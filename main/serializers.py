from rest_framework import serializers
from main.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    sections = serializers.StringRelatedField(read_only=True, many=True)
    class Meta:
        model = Category
        fields = ('id', 'name','sections','image')

class ImageSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name', read_only=True)
    class Meta:
        model = Image
        fields = ['id','image','product']

class SectionSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name',read_only=True)
    class Meta:
        model = Section
        fields = ['id','name','image','category']

class ProductSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    section_name = serializers.CharField(source='section.name',read_only=True)
    avg_rating = serializers.FloatField(read_only=True)
    class Meta:
        model = Product
        fields = ('id','name','description','price','comments','avg_rating','images','section','section_name')