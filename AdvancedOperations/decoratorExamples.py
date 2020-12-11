import functools
import logging, os, tempfile

# 不带参数函数修饰器
def positive_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        assert result >= 0, func.__name__ + "() result isn't >=0"
        return result
    return wrapper

@positive_result
def descriminant(a, b, c):
    return (b ** 2) - (4 * a * c)


# 带参数函数修饰器
def bounded(minimum, maximum):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result < minimum:
                return minimum
            elif result > maximum:
                return maximum
            return result
        return wrapper
    return decorator

@bounded(0, 100)
def percent(amount, total):
    return (amount / total) * 100


if __name__ == '__main__':
    # testResult = descriminant(4, 5, 3) # AssertionError: descriminant() result isn't >=0
    testResult2 = descriminant(4, 8, 3) #
    testResult3 = percent(20, 5) # 100
    print(f"percent(20, 5): {testResult3}")

if __name__ == '__debug__':
    logger = logging.getLogger("Logger")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(os.path.join(tempfile.gettempdir(), 'logged.log'))
    logger.addHandler(handler)

    def logged(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log = "called: " + func.__name__ + "("
            log += ",".join(["{0!r}".format(a) for a in args] +
                            ["{0!s}={1!r}".format(k, v) for k, v in kwargs.items()])
            result = exception = None

            try:
                result = func(*args, **kwargs)
                return result
            except Exception as err:
                exception = err
            finally:
                log += (
                    (") ->" + str(result)) if exception is None else ") {0}: {1}".format(type(exception), exception)
                )
                logger.debug(log)
                if exception is not None:
                    raise exception
        return wrapper
else:
    def logged(function):
        return function


@logged
def discounted_price(price, percentage, make_integer=False):
    result = price * ((100 - percentage) / 100)
    if not (0 < result <= price):
        raise ValueError("invalid price")
    return result if not make_integer else int(round(result))

