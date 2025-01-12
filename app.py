from fastapi import FastAPI, WebSocket, HTTPException
from typing import Union
import uvicorn

from services import ParserService
from handlers import ParserHandlers
from websocket import WebSocketManager
from dto import DataSchemaOut


class App:
    def __init__(
        self,
        parser_service: ParserService,
        websocket_manager: WebSocketManager,
        handlers: ParserHandlers,
    ):
        self.parser = parser_service
        self.websocket_manager = websocket_manager
        self.handlers = handlers
        self.app = FastAPI()
        self._add_routes()

    def _add_routes(self):
        self.app.get("/data/", response_model=list[DataSchemaOut])(
            self.handlers.get_all_data
        )
        self.app.get(
            "/data/{item_id}",
            responses={
                200: {"model": DataSchemaOut},
                404: {"description": "Данные не найдены"}
            }
        )(self.handlers.get_data)
        self.app.put(
            "/data/{item_id}",
            responses={
                200: {"model": DataSchemaOut},
                404: {"description": "Данные не найдены"}
            }
        )(self.handlers.update_data)
        self.app.delete(
            "/data/{item_id}",
            responses={
                200: {"description": "Данные успешно удалены"},
                404: {"description": "Данные не найдены"}
            }
        )(self.handlers.delete_data)
        self.app.post(
            "/data/",
            responses={
                200: {"description": "Данные успешно созданы"}
            }
        )(self.handlers.create_data)
        self.app.add_event_handler("startup", self.handlers.startup)
        self.app.websocket("/ws")(self.websocket_endpoint)

    async def websocket_endpoint(self, websocket: WebSocket):
        print("Попытка подключения к WebSocket")
        await self.websocket_manager.connect(websocket)
        try:
            while True:
                data = await websocket.receive_text()
                print(f"Получено сообщение: {data}")
        except Exception as e:
            print(f"Ошибка WebSocket: {e}")
            self.websocket_manager.disconnect(websocket)

    def run(self):
        uvicorn.run(self.app, host="0.0.0.0", port=8000)

parser_service = ParserService("HENDERSON")
websocket_manager = WebSocketManager()
parser_handlers = ParserHandlers(parser_service, websocket_manager)

app = App(parser_service, websocket_manager, parser_handlers)
app.run()

# uvicorn app:app --reload
