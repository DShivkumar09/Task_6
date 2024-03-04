from rest_framework.views import APIView
import pandas as pd
from .models import Product
from .serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# Create your views here.

class UploadExcel(APIView):
    def post(self, request):
        try:
            excel_file = request.data.get('file')
            df = pd.read_excel(excel_file)
            df.dropna(how='all', axis=1, inplace=True)
            inserted_records = []
            if 'product_manufacturing_date' in df.columns:
                df['product_manufacturing_date'] = df['product_manufacturing_date'].dt.date
            if 'product_expiry_date' in df.columns:
                df['product_expiry_date'] = df['product_expiry_date'].dt.date
            for index, row in df.iterrows():
                print(row)
                product_id = row['product_id']
                if not Product.objects.filter(product_id=product_id).exists():
                    serializer = ProductSerializer(data=row.to_dict())
                    if serializer.is_valid():
                        serializer.save()
                        inserted_records.append(serializer.data)
            return Response({"message": "Records inserted successfully", "inserted_records": \
                         inserted_records}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            print(e)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all().order_by('product_category')
    serializer_class = ProductSerializer
 