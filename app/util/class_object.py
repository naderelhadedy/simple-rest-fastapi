"""
helper classes
"""


def singleton(class_):
    """
    singleton design pattern
    """
    instances = {}

    def getinstance(*args, **kwargs):
        """
        get instance
        """
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance
