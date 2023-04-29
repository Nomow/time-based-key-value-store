from sqlalchemy.orm import Session
from unittest import TestCase
from unittest.mock import create_autospec, patch
from app.repositories.time_map_repository import TimeMapRepository

class TestTimeMapRepository(TestCase):

    def setUp(self):
        super().setUp()
        self.session : Session = create_autospec(Session)
        self.time_map_repository : TimeMapRepository = TimeMapRepository(self.session)

    @patch("app.models.time_map_model.TimeMapModel", autospec = True)
    def test_should_call_get_session_method_once_in_get_method(self, TimeMapModel):
        time_map_instance = TimeMapModel(timestamp = "123456", key = "value")
        self.time_map_repository.get(time_map_instance)
        self.session.get.assert_called_once()

    @patch("app.models.time_map_model.TimeMapModel", autospec = True)
    def test_should_call_merge_session_method_once_in_put_method(self, TimeMapModel):
        time_map_instance = TimeMapModel(timestamp = "123456", key = "value", value = "value")
        self.time_map_repository.put(time_map_instance)
        self.session.merge.assert_called_once_with(time_map_instance)

