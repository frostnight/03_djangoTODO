from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    # def create(self, validated_data):
    #     return Book.objects.create(**validated_data)
    #
    # def update(self, instance: Book, validated_data: dict):
    #     instance = validated_data.get('bid', instance.bid)
    #     instance = validated_data.get('title', instance.title)
    #     instance = validated_data.get('author', instance.author)
    #     instance = validated_data.get('category', instance.category)
    #     instance = validated_data.get('pages', instance.pages)
    #     instance = validated_data.get('price', instance.price)
    #     instance = validated_data.get('published_date', instance.published_date)
    #     instance = validated_data.get('description', instance.description)
    #     instance.save()
    #
    #     return instance

    class Meta:
        model = Book
        fields = ['bid', 'title', 'author', 'category', 'pages', 'price', 'published_date', 'description']
