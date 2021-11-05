from .models import Account, AccountSerializer
from users.models import User

class AccountServices:
    def new_account(self, request):
        
        try:
            data = AccountSerializer.data(request.body)
            _user_id = data.get('user_id')
            user_instance = User.objects.filter(user_id = _user_id).first()
            id = Account.objects.all().reverse().values('account_id').first()
            if id:
                id = id.get('account_id')[1:]
            else:
                id = 0
            _account_id = f'S{int(id)+1:0>5}'
            Account.objects.create(account_id=_account_id, user_id=user_instance)
            return f'Account {_account_id} successfuly created!'
        
        except ValueError as exc:
            return exc 
