from tethys_sdk.base import TethysAppBase, url_map_maker


class Covid(TethysAppBase):
    """
    Tethys app class for COVID 19.
    """

    name = 'COVID 19'
    index = 'covid:home'
    icon = 'covid/images/logo.png'
    package = 'covid'
    root_url = 'covid'
    color = '#000000'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='covid',
                controller='covid.controllers.home'
            ),
        )

        return url_maps