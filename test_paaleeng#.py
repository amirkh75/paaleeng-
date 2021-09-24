import pytest


from api import API

# use 'pytest paaleeng#.py' for test.
@pytest.fixture
def api():
    """explaine here..."""
    return API()

def test_basic_route(api):
    """explaine here..."""
    @api.route('/home')
    def home(request, response):
        response.text = 'YOLO'


def test_basic_overlap_throws_exception(api):
    """explaine here..."""
    @api.route('/home')
    def home(request, response):
        response.text = 'YOLO'

    with pytest.raises(AssertionError):
        @api.route('/home')
        def home2(request, response):
            response.text = 'YOLO'