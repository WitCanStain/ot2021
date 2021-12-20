from pygame import Vector2
def scale_mouse(pos, screen, fake_screen):
        """Scales mouse coordinates so that the correct coordinates are produced even if
        player resizes window.

        Args:
            pos: position of the mouse cursor.

        Returns:
            scaled_pos: the scaled coordinates of the mouse cursor.
        """
        ratio_x = screen.get_rect().width / fake_screen.get_rect().width
        ratio_y = screen.get_rect().height / fake_screen.get_rect().height
        scaled_pos = Vector2(pos[0] / ratio_x, pos[1] / ratio_y)
        return scaled_pos