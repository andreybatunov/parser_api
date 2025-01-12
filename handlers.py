from services import ParserService
from dto import DataSchemaIn
from websocket import WebSocketManager
from fastapi import HTTPException

class ParserHandlers:
    def __init__(
        self, parser_service: ParserService, websocket_manager: WebSocketManager
    ):
        self.parser_service = parser_service
        self.websocket_manager = websocket_manager

    async def get_all_data(self):
        try:
            data = self.parser_service.get_all_data()
            await self.websocket_manager.broadcast("GET Запрос на получение всех данных")
            return data
        except Exception as e:
            await self.websocket_manager.broadcast(f"Ошибка получения всех данных: {e}")

    async def create_data(self, data: DataSchemaIn):
        try:
            self.parser_service.create_data(data)
            await self.websocket_manager.broadcast("POST Запрос на создание данных")
            return {"status": "success", "message": "Данные успешно созданы"}
        except Exception as e:
            await self.websocket_manager.broadcast(f"Ошибка создания данных: {e}")

    async def get_data(self, item_id: int):
        try:
            data = self.parser_service.get_data(item_id)
            await self.websocket_manager.broadcast(f"GET Запрос на получение данных c id: {item_id}")
            return data
        except Exception as e:
            await self.websocket_manager.broadcast(f"Ошибка получения данных: {e}")
            raise HTTPException(status_code=404, detail="Данные не найдены")

    async def update_data(self, item_id: int, data: DataSchemaIn):
        try:
            updated_data = self.parser_service.update_data(item_id, data)
            await self.websocket_manager.broadcast(f"PUT Запрос на обновление данных c id: {item_id}")
            return updated_data
        except Exception as e:
            await self.websocket_manager.broadcast(f"Ошибка обновления данных: {e}")
            raise HTTPException(status_code=404, detail="Данные не найдены")

    async def delete_data(self, item_id: int):
        try:
            self.parser_service.delete_data(item_id)
            await self.websocket_manager.broadcast(f"DELETE Запрос на удаление данных c id: {item_id}")
            return {"status": "success", "message": "Данные успешно удалены"}  
        except Exception as e:
            await self.websocket_manager.broadcast(f"Ошибка удаления данных: {e}")
            raise HTTPException(status_code=404, detail="Данные не найдены")
        
    async def startup(self):
        await self.parser_service.startup()
