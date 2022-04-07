import pytest
from Src.PageObject.j_pet_store_page import Home


class TestJpetStore:
    @pytest.fixture()
    def setup(self):
        self.url = "https://petstore.octoperf.com/"
        self.home = Home(self.url)
        yield self.home


    def test_heading_title(self, setup):
        heading_title = setup.get_heading()
        assert heading_title == "Welcome to JPetStore 6"
