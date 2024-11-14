from library import Library, LibraryException


def main():
    library = Library()

    library.load_library_data()

    library.add_book("Python for beginning", "Unknown")
    library.register_user(1, "Maksym")

    try:
        library.checkout_book(1, "Python for beginning")
    except LibraryException as exp:
        print(exp)

    library.save_library_data()


if __name__ == "__main__":
    main()
