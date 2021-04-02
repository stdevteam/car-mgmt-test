from flask import request
from flask_restplus import Resource

from customer.service.customer_service import (
    get_all_customers,
    add_new_customer,
    get_customer,
    update_customer,
    delete_customer
)
from customer.utils.dto import CustomerDto
from flask_restplus._http import HTTPStatus

api = CustomerDto.api
_customer = CustomerDto.customer


@api.route('/')
class CustomerList(Resource):
    @api.doc('list_of_customers')
    @api.marshal_list_with(_customer, envelope='data')
    def get(self):
        """ Ist all registered customers """
        return get_all_customers()

    @api.response(HTTPStatus.CREATED, 'Customer successfully created.')
    @api.doc('create a new customer')
    @api.expect(_customer, validate=True)
    def post(self):
        """Creates a new Customer """
        data = request.json
        return add_new_customer(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Customer identifier')
@api.response(404, 'Customer not found.')
class Customer(Resource):
    @api.doc('get a customer')
    @api.marshal_with(_customer)
    def get(self, public_id):
        """get a customer given its identifier"""
        customer = get_customer(public_id)
        if not customer:
            api.abort(404)
        else:
            return customer

    @api.doc('update a customer')
    @api.expect(_customer, validate=True)
    def put(self, public_id):
        """update a customer"""
        customer = get_customer(public_id)
        if not customer:
            api.abort(404)
        else:
            data = request.json
            return update_customer(public_id, data)

    @api.doc('delete a customer')
    @api.marshal_with(_customer)
    def delete(self, public_id):
        """delete a customer"""
        customer = get_customer(public_id)
        if not customer:
            api.abort(404)
        else:
            return delete_customer(public_id)


