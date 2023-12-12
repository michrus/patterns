from abc import ABC, abstractmethod


class CheckWhatsWhatOutboundBoundary(ABC):
    def __init__(self) -> None:
        self._response = None

    @abstractmethod
    def form_response(self, whats_what: bool):
        pass

    @property
    def response(self):
        return self._response
