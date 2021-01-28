from controllers.my_animes_controller import my_anime               # importing the my_anime blueprint
from controllers.auth_controller import auth                        # importing the authentication blueprint (user)
from controllers.profile_images_controller import profile_images    # importing the profile images blueprint
from controllers.user_controller import user                        # importing the user blueprint 

registerable_controllers = [
    auth,
    my_anime,
    profile_images,
    profiles
]