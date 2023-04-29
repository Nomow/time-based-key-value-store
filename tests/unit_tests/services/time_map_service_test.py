from unittest import TestCase
from unittest.mock import create_autospec, patch
from app.repositories.time_map_repository import TimeMapRepository
from app.services.time_map_service import TimeMapService

class TestTimeMapService(TestCase):

    def setUp(self):
        super().setUp()

        self.time_map_repository : TimeMapRepository = create_autospec(TimeMapRepository)
        self.time_map_service : TimeMapService = TimeMapService(self.time_map_repository)

    @patch("app.schemas.time_map_schema.TimeMapKeyTimestampSchema", autospec = True)
    def test_should_call_repository_get_method_once_in_get_method(self, TimeMapKeyTimestampSchema):
        time_map_schema = TimeMapKeyTimestampSchema()
        time_map_schema.key = "key"
        time_map_schema.timestamp = "2023-04-29T21:13:35.597Z"

        self.time_map_service.get(time_map_schema)
        self.time_map_repository.get.assert_called_once()

    @patch("app.schemas.time_map_schema.TimeMapKeyTimestampSchema", autospec = True)
    def test_should_call_repository_get_method_once_in_exists_method(self, TimeMapKeyTimestampSchema):
        time_map_schema = TimeMapKeyTimestampSchema()
        time_map_schema.key = "key"
        time_map_schema.timestamp = "2023-04-29T21:13:35.597Z"

        self.time_map_service.exists(time_map_schema)
        self.time_map_repository.get.assert_called_once()

    @patch("app.schemas.time_map_schema.TimeMapSchema", autospec = True)
    def test_should_call_repository_put_method_once_in_put_method(self, TimeMapSchema):
        time_map_schema = TimeMapSchema()
        time_map_schema.key = "key"
        time_map_schema.timestamp = "2023-04-29T21:13:35.597Z"
        time_map_schema.value = "value"

        self.time_map_service.put(time_map_schema)
        self.time_map_repository.put.assert_called_once()

