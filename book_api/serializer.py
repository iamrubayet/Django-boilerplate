# from rest_framework import serializers
# from book_api.models import Books

# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     number_of_pages = serializers.IntegerField()
#     published_date = serializers.DateField()
#     quantity = serializers.IntegerField()

#     def create(self,data):
#         return Books.objects.create(**data)
#     def update(self,instance,data):
#         instance.title = data.get('title',instance.title)
#         instance.number_of_pages = data.get('number_of_pages',instance.number_of_pages)
#         instance.published_date = data.get('published_date',instance.published_date)
#         instance.quantity = data.get('quantity',instance.quantity)
#         instance.save()
#         return instance

from rest_framework import serializers
from book_api.models import Books
from django.forms import ValidationError

class BookSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    class meta:
        model = Books
        fields = '__all__'
    
    def validate_title(self,value):
        if value == 'Diet Coke':
            raise ValidationError('Diet Coke is not allowed')
        return value
    def validate(self,data):
        if data['quantity'] < 0:
            raise ValidationError('Quantity cannot be negative')
        return data
    def get_description(self,data):
        return "this book is called"+ data.title + "and it is" + str(data.number_of_pages) + "pages long"

    


