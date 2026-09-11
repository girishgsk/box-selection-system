from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import BoxRecommendationSerializer
from .services import recommend_box


@api_view(["POST"])
def recommend_box_api(request):

    serializer = BoxRecommendationSerializer(
        data=request.data
    )

    if not serializer.is_valid():
        return Response(
            {
                "error": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    products = serializer.validated_data["products"]

    try:
        box = recommend_box(products)

    except Exception as error:
        return Response(
            {
                "error": str(error)
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    if box is None:
        return Response(
            {
                "message": "No suitable box found"
            },
            status=status.HTTP_404_NOT_FOUND
        )

    return Response(
        {
            "recommended_box": {
                "id": box.id,
                "name": box.name,
                "length": box.length,
                "width": box.width,
                "height": box.height,
                "max_weight": box.max_weight,
                "cost": box.cost
            }
        },
        status=status.HTTP_200_OK
    )