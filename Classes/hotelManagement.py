import importlib.util as ut
import sys

spec = ut.spec_from_file_location('hotel', 'D:\Python\Workouts\Classes\hotel.py')
foo = ut.module_from_spec(spec)

sys.modules['hotel'] = foo
spec.loader.exec_module(foo)

hotel = foo.Restaurant()

# hotel.add