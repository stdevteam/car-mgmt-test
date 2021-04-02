from flask import current_app
from flask_restplus._http import HTTPStatus

from customer.utils.wrappers import db_operation


@db_operation()
def check_if_exists(email, cursor):
    sql = "SELECT `id` FROM `customer` WHERE `email`=%s"
    cursor.execute(sql, (email, ))
    return cursor.fetchone()


@db_operation(True)
def create_customer(data, cursor):
    sql = f"INSERT INTO `customer` {tuple(data.keys())} VALUES (%s, %s, %s)"
    cursor.execute(sql, tuple(data.values()))


def add_new_customer(data):
    email = data["email"]
    customer = check_if_exists(email)
    if not customer:
        try:
            create_customer(data)
        except Exception as e:
            current_app.logger.error(e)
            return {
                'status': 'fail',
                'message': 'Something went wrong!'
            }, HTTPStatus.BAD_REQUEST

        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, HTTPStatus.CREATED
    else:
        response_object = {
            'status': 'fail',
            'message': 'Customer already exists.',
        }
        return response_object, HTTPStatus.CONFLICT


@db_operation()
def get_customer(customer_id, cursor):
    sql = "SELECT * FROM `customer` WHERE `id`=%s"
    cursor.execute(sql, (customer_id, ))
    return cursor.fetchone()


@db_operation(True)
def update_customer(customer_id, data, cursor):
    update_string = ""
    for item in data.keys():
        update_string += f"{item}='{data[item]}', "
    sql = f"UPDATE `customer` SET {update_string[:-2]} WHERE `id`=%s"
    cursor.execute(sql, (customer_id, ))

    return {
        'status': 'success',
        'message': 'Successfully updated.'
    }, HTTPStatus.OK


@db_operation(True)
def delete_customer(customer_id, cursor):
    sql = f"DELETE FROM `customer` WHERE `id`=%s"
    cursor.execute(sql, (customer_id, ))

    return {
        'status': 'success',
        'message': 'Successfully deleted.'
    }, HTTPStatus.OK



@db_operation()
def get_all_customers(cursor):
    sql = "SELECT * FROM `customer`"
    cursor.execute(sql)
    return cursor.fetchall()
