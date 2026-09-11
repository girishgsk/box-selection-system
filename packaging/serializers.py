from rest_framework import serializers


class ProductItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(min_value=1)
    quantity = serializers.IntegerField(min_value=1)


class BoxRecommendationSerializer(serializers.Serializer):
    products = ProductItemSerializer(many=True)

    def validate_products(self, value):
        if not value:
            raise serializers.ValidationError(
                "At least one product is required."
            )

        return value