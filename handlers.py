from services import ParserService
from dto import DataSchemaIn
from websocket import WebSocketManager


class ParserHandlers:
    def __init__(
        self, parser_service: ParserService, websocket_manager: WebSocketManager
    ):
        self.parser_service = parser_service
        self.websocket_manager = websocket_manager

    async def get_all_data(self):
        try:
            data = self.parser_service.get_all_data()
            await self.websocket_manager.broadcast(
                "\n".join([str(item) for item in data])
            )
            return data
        except Exception as e:
            await self.websocket_manager.broadcast(f"Ошибка получения всех данных: {e}")

    async def get_data(self, item_id: int):
        try:
            data = self.parser_service.get_data(item_id)
            await self.websocket_manager.broadcast(
                f"Получены данные с id: {item_id}: {str(data)}"
            )
            return data
        except Exception as e:
            await self.websocket_manager.broadcast(f"Ошибка получения данных: {e}")

    async def update_data(self, item_id: int, data: DataSchemaIn):
        try:
            updated_data = self.parser_service.update_data(item_id, data)
            await self.websocket_manager.broadcast(
                f"Обновлены данные: {str(updated_data)}"
            )
            return updated_data
        except Exception as e:
            await self.websocket_manager.broadcast(f"Ошибка обновления данных: {e}")

    async def delete_data(self, item_id: int):
        try:
            self.parser_service.delete_data(item_id)
            await self.websocket_manager.broadcast(f"Удалены данные c id: {item_id}")
        except Exception as e:
            await self.websocket_manager.broadcast(f"Ошибка удаления данных: {e}")

    async def startup(self):
        await self.parser_service.startup()
