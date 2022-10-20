from controller.controller_border import BorderController
from controller.controller_rarity import RarityController
from controller.controller_tag import TagController


def test_tag():
    controller = TagController()

    print("Testing Tag")
    print("Report")
    controller.list_table()


def test_rarity():
    controller = RarityController()

    print("\n\nTesting Rarity")
    print("Report")
    controller.list_table()

    print("\nUpdate SQL")
    print(controller._generate_update_sql(1, "Testing", 2))


def test_border():
    controller = BorderController()

    print("\n\nTesting Border")
    print("Report")
    controller.list_table()

    print("\nInsert SQL")
    print(controller._generate_insert_sql("Testing", 2, "image.png"))
    print(controller._generate_insert_sql("Testing", 2, None))

    print("\nUpdate SQL")
    print(controller._generate_update_sql(1, "Testing", "image.png", 2))


if __name__ == "__main__":
    test_tag()
    test_rarity()
    test_border()
