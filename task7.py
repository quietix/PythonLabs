class B:
    @staticmethod
    def stat_print_dict(class_obj: object):
        print(f"Class object attributes: {class_obj.__dict__}")

    @classmethod
    def cls_print_dict(cls):
        print(f"Attributes of {cls.__name__}: {cls.__dict__}")

class C(B):
    e = "Клас С"


if __name__ == "__main__":
    obj = B()
    obj.stat_print_dict(obj)
    obj.cls_print_dict()

    obj_1 = B()
    obj_1.stat_print_dict(obj_1)
    obj_1.cls_print_dict()

    obj_2 = C()
    obj_2.stat_print_dict(obj_2)
    obj_2.cls_print_dict()

