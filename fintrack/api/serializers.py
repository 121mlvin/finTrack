from rest_framework import serializers
from django.contrib.auth.models import User
from allauth.account.utils import setup_user_email
from core.models import Account, Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'user', 'date_of_spending', 'price', 'description', 'expense_type']
        read_only_fields = ['id', 'date_of_spending', 'user']


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    profile_picture = serializers.ImageField(required=False)
    balance = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Username already exists")
        return username

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")
        return email

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        print("Creating user with data:", validated_data)
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password1'])
        user.save()

        setup_user_email(self.context['request'], user, [])

        account = Account.objects.create(
            user=user,
            balance=validated_data['balance'],
            profile_picture=validated_data.get('profile_picture')
        )

        print("User created:", user)
        print("Account created:", account)

        return user
