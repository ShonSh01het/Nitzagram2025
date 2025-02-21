import pygame

from constants import *
from helpers import screen



class Post:
    """
    A class used to represent post on Nitzagram
    """

    def __init__(self, user_name, location, likes_counter, comments, description):
        self.user_name = user_name
        self.location = location
        self.likes_counter = likes_counter
        self.comments = comments
        self.description = description

    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        myfont = pygame.font.Font('fonts/Roboto_Condensed-Black.ttf', 15)
        write_user = myfont.render(str(self.user_name), True, BLACK)
        screen.blit(write_user, (USER_NAME_X_POS, USER_NAME_Y_POS))
        write_location = myfont.render(str(self.location), True, LIGHT_GRAY)
        screen.blit(write_location, (USER_NAME_X_POS, USER_NAME_Y_POS + 15))
        write_likes_counter = myfont.render("Liked by " + str(self.likes_counter) + " users", True, GREY)
        screen.blit(write_likes_counter, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))
        write_description = myfont.render(str(self.description), True, BLACK)
        screen.blit(write_description, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))
        COMMENT_X_POS = FIRST_COMMENT_X_POS
        COMMENT_Y_POS = FIRST_COMMENT_Y_POS
        if len(self.comments) >= NUM_OF_COMMENTS_TO_DISPLAY:
            for comment in range(NUM_OF_COMMENTS_TO_DISPLAY):
                write_comment = myfont.render(str(self.comments[comment]), True, GREY)
                screen.blit(write_comment, (COMMENT_X_POS, COMMENT_Y_POS))
                COMMENT_Y_POS += 15
        else:
            for comment in range(len(self.comments)):
                write_comment = myfont.render(str(self.comments[comment]), True, GREY)
                screen.blit(write_comment, (COMMENT_X_POS, COMMENT_Y_POS))
                COMMENT_Y_POS += 15


class Image_Post(Post):
    def __init__(self, image, user_name, location, likes_counter, comments, description):
        super().__init__(user_name, location, likes_counter, comments, description)
        self.image = image

    def display(self):
        super().display()
        post_image = pygame.image.load(self.image)
        small_image = pygame.transform.smoothscale(post_image, (POST_WIDTH, POST_HEIGHT))
        screen.blit(small_image, (POST_X_POS, POST_Y_POS))


class Text_Post(Post):
    def __init__(self, text, color, backgraund_color, user_name, location, likes_counter, comments, description):
        super().__init__(user_name, location, likes_counter, comments, description)
        self.text = text
        self.color = color
        self.backgraund_color = backgraund_color

    def display(self):
        super().display()
        backgraund = pygame.Surface((POST_WIDTH, POST_HEIGHT))
        backgraund.fill(self.backgraund_color)
        screen.blit(backgraund, (POST_X_POS, POST_Y_POS))
        myfont = pygame.font.Font('fonts/Roboto_Condensed-Black.ttf', TEXT_POST_FONT_SIZE)
        write_post = myfont.render(str(self.text), True, self.color, self.backgraund_color)
        screen.blit(write_post, (POST_X_POS, POST_Y_POS))


    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break


