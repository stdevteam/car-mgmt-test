import functools

from customer import db

from customer.utils.dto import CustomerDto
from flask import current_app

api = CustomerDto.api


def db_operation(is_update=False):
    def inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            db.ping(reconnect=True)
            with db:
                with db.cursor() as cursor:
                    try:
                        result = func(*args, cursor=cursor, **kwargs)
                    except Exception as e:
                        current_app.logger.error(e)
                        db.rollback()
                        # log
                        return {
                            'status': 'fail',
                            'message': 'Something went wrong.'
                        }, 400
                if is_update:
                    db.commit()
                return result
        return wrapper
    return inner
