from budget.db import get_connection, create_data_path


def main() -> None:
    create_data_path()
    get_connection()


if __name__ == "__main__":
    main()
