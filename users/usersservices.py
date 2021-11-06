from .models import User, UserSerialize


class UsersServices:
    def all_users(self):
        model = User.objects.all()
        return UserSerialize.data(model)


    def user_details(self, id):
        try:
            model = User.objects.filter(user_id = int(id))
            return UserSerialize.data(model)
        except ValueError as exc:
            return exc


    def new_user(self, request):
        try:
            data = UserSerialize.data(request.body)
            _name = data.get('name')
            _email = data.get('email')
            _age = data.get('age')
            User.objects.create(name = _name, email = _email, age = _age)
            return f'Success user {_name} created !'
        except ValueError as exc:
            return exc
