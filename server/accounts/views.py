from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

# Get the user model
User = get_user_model()

class LoginView(APIView):
    """
    View to handle user login and generate JWT tokens.
    """
    
    def post(self, request):
        # Extract username and password from the request
        username = request.data.get("username")
        password = request.data.get("password")

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is None:
            raise AuthenticationFailed("Invalid credentials")

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        # Serialize user data
        serializer = UserSerializer(user)
        user_data = serializer.data

        # Return tokens and user data
        return Response(
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "user": user_data,
            }
        )

class LogoutView(APIView):
    """
    View to handle user logout and blacklist the refresh token.
    """
    
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            # Extract refresh token from the request
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response(
                    {"error": "Refresh token is required."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Blacklist the refresh token
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"success": "User logged out successfully."},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class UserViewSet(ModelViewSet):
    """
    ViewSet to handle CRUD operations for users.
    """
    
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Validate and deserialize input
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extract role and determine rank
        role = serializer.validated_data["role"]
        rank = self.get_rank_for_role(role)

        # Create a new user instance
        new_user = User(
            username=serializer.validated_data["username"],
            first_name=serializer.validated_data["first_name"],
            last_name=serializer.validated_data["last_name"],
            role=role,
            rank=rank,
        )

        # Check if the requesting user has permission to create a user with the requested rank
        if not self.can_create_user_with_rank(request.user, rank):
            raise PermissionDenied(
                "You don't have permission to create a user with this role."
            )

        # Set user password and save
        new_user.set_password(serializer.validated_data["password"])
        new_user.save()

        # Return response with newly created user data
        headers = self.get_success_headers(serializer.data)
        return Response(
            self.serializer_class(new_user).data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    def get_queryset(self):
        """
        Returns the queryset for the users based on the requesting user's permissions.
        """
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(rank__lte=self.request.user.rank)

    def get_rank_for_role(self, role):
        """
        Returns the rank associated with a given role.
        """
        if role == User.ROLE_ADMIN:
            return 4
        elif role in [User.ROLE_HOKIM, User.ROLE_HOKIM_YORDAMCHISI]:
            return 3
        elif role in [User.ROLE_TUMAN_MASUL, User.ROLE_TUMAN_YOSHLAR_ISHLARI]:
            return 2
        elif role in [User.ROLE_MAHALLA_MASUL, User.ROLE_MAKTAB_MASUL]:
            return 1
        else:
            raise ValueError(f"Unknown role: {role}")

    def can_create_user_with_rank(self, user, requested_rank):
        """
        Determines if the requesting user can create a user with the specified rank.
        """
        if user.is_superuser:
            return True

        if user.rank > requested_rank:
            return True

        return False
