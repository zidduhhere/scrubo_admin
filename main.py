import os
import pathlib


def create_paths(path_list):
    """
    Creates folders and files specified in a list of paths.

    Args:
        path_list: A list of strings, where each string is a full path
                   to a file or folder to be created.
                   e.g., ["/tmp/myfolder", "/tmp/myfile.txt", "/home/user/anotherfolder/file2.log"]

    """
    for path_str in path_list:
        path = pathlib.Path(path_str)  # Use pathlib for better path handling

        try:
            if path.suffix:  # Check if it should be a file
                # Create parent directories if they don't exist.
                path.parent.mkdir(parents=True, exist_ok=True)
                path.touch()  # Create an empty file
                print(f"File created: {path}")

            else:  # Check if it should be a folder
                path.mkdir(parents=True, exist_ok=True)
                print(f"Folder created: {path}")

        except OSError as e:
            print(f"Error creating '{path_str}': {e}")


# Example usage:#
# paths_to_create = [
# "/tmp/myproject/data",  # Folder
# "/tmp/myproject/data/file1.csv",  # File
# "/tmp/myproject/scripts/process.py",  #File
# "/home/user/documents/report.pdf"
folders_and_files = [
    "lib/models/user_model.dart",
    "lib/models/service_model.dart",
    "lib/models/booking_model.dart",
    "lib/models/review_model.dart",
    "lib/views/login/login_view.dart",
    "lib/views/login/signup_view.dart",
    "lib/views/home/home_view.dart",
    "lib/views/service_details/service_details_view.dart",
    "lib/views/service_scheduling/service_scheduling_view.dart",
    "lib/views/payment/payment_view.dart",
    "lib/views/booking_history/booking_history_view.dart",
    "lib/views/profile_management/profile_management_view.dart",
    "lib/views/ratings_reviews/ratings_reviews_view.dart",
    "lib/viewmodels/login/login_viewmodel.dart",
    "lib/viewmodels/login/signup_viewmodel.dart",
    "lib/viewmodels/home/home_viewmodel.dart",
    "lib/viewmodels/service_details/service_details_viewmodel.dart",
    "lib/viewmodels/service_scheduling/service_scheduling_viewmodel.dart",
    "lib/viewmodels/payment/payment_viewmodel.dart",
    "lib/viewmodels/booking_history/booking_history_viewmodel.dart",
    "lib/viewmodels/profile_management/profile_management_viewmodel.dart",
    "lib/viewmodels/ratings_reviews/ratings_reviews_viewmodel.dart",
    "lib/services/auth_service.dart",
    "lib/services/booking_service.dart",
    "lib/services/payment_service.dart",
    "lib/services/review_service.dart",
    "lib/utils/constants.dart",
    "lib/utils/helpers.dart",
]

create_paths(folders_and_files)
