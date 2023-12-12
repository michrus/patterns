from ..application.interfaces.check_whats_what_outbound \
    import CheckWhatsWhatOutboundBoundary


class CheckWhatsWhatApiPresenter(CheckWhatsWhatOutboundBoundary):
    def __init__(self) -> None:
        super().__init__()

    def form_response(self, whats_what: bool) -> None:
        self._response = {
            'data': {
                'whatIsWhat': 'True' if whats_what else 'False'
            }
        }
