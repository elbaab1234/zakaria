from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.button import Button
from kivy.core.window import Window

KV = '''
ScreenManager:
    Screen:
        name: "screen 0"
        BoxLayout:
            orientation: 'vertical'
            padding:20
            spacing:20
            Button:
                background_normal: 'image1.png'
                background_down: 'down.png'
                size_hint: (1, .9)
                pos_hint: {"center_x": 0.5,"center_y": 0.9} 
            Button:
                size_hint: 1, 0.1
                text: "Entrer"
                font_size: 22
                pos_hint: {"center_x": .5}
                on_release:
                    root.current = "screen A"
    Screen:
        name: "screen A"
        Button:
            background_normal: 'imageA.png'
            background_down: 'down.png'
            size_hint: (1, .3)
            pos_hint: {"center_x": 0.5,"center_y": 0.9}
        Label:
            text:'Langage Python'
            halign: "center"
            font_size: self.width/15
            pos_hint: {"center_x": 0.5,"center_y": 0.7}
        Button:
            text: "Introduction"
            pos_hint: {"center_x": .5}
            size_hint: (0.6, 0.08)
            pos_hint: {'center_x':0.5, 'center_y':0.6}
            font_size : 28
            on_release:
                root.current = "screen B"
        Button:
            text: "Variables"
            pos_hint: {"center_x": .5}
            size_hint: (0.6, 0.08)
            pos_hint: {'center_x':0.5, 'center_y':0.51}
            font_size : 28
            on_release:
                root.current = "screen C"
        Button:
            text: "Langage Python"
            pos_hint: {"center_x": .5}
            size_hint: (0.6, 0.08)
            pos_hint: {'center_x':0.5, 'center_y':0.42}
            font_size : 28
            on_release:
                root.current = "screen E"
        Button:
            text: "Conditions"
            pos_hint: {"center_x": .5}
            size_hint: (0.6, 0.08)
            pos_hint: {'center_x':0.5, 'center_y':0.33}
            font_size : 28
            on_release:
                root.current = "screen E"
        Button:
            text: "Boucles"
            pos_hint: {"center_x": .5}
            size_hint: (0.6, 0.08)
            pos_hint: {'center_x':0.5, 'center_y':0.24}
            font_size : 28
            on_release:
                root.current = "screen F"
        Button:
            text: "Web"
            pos_hint: {"center_x": .5}
            size_hint: (0.6, 0.08)
            pos_hint: {'center_x':0.5, 'center_y':0.15}
            font_size : 28
            on_release:
                root.current = "screen G"
        Button:
            text: "Quiter"
            pos_hint: {"center_x": .5}
            size_hint: (0.9, 0.08)
            pos_hint: {'center_x':0.5, 'center_y':0.06}
            font_size : 28
            on_release:
                app.Open_dialog()
               
    Screen:
        name: "screen B"
        BoxLayout:
            padding:12
            spacing:3
            orientation: 'vertical'
            Button:
                text: "Introduction"
                font_size : 28
                size_hint: (1, 0.1)
            Button:
                background_normal: 'imageB.png'
                background_down: 'down.png'
                size_hint: (1, .8)
                pos_hint: {"center_x": 0.5,"center_y": 0.5}
            Button:
                text: "Retour"
                font_size : 28
                size_hint: (1, 0.1)
                on_release:
                    root.current = "screen A"
    Screen:
        name: "screen C"
        BoxLayout:
            padding:12
            spacing:3
            orientation: 'vertical'
            Button:
                text: "Variables"
                font_size : 20
                size_hint: (1, 0.1)
            Button:
                background_normal: 'imageC.png'
                background_down: 'down.png'
                size_hint: (1, .8)
                pos_hint: {"center_x": 0.5,"center_y": 0.5}
            Button:
                text: "Retour"
                font_size : 19
                size_hint: (1, 0.1)
                on_release:
                    root.current = "screen A"
    Screen:
        name: "screen D"
        BoxLayout:
            padding:12
            spacing:3
            orientation: 'vertical'
            Button:
                text: "Operations"
                font_size : 20
                size_hint: (1, 0.1)
            Button:
                background_normal: 'imageD.png'
                background_down: 'down.png'
                size_hint: (1, .8)
                pos_hint: {"center_x": 0.5,"center_y": 0.5}
            Button:
                text: "Retour"
                font_size : 19
                size_hint: (1, 0.1)
                on_release:
                    root.current = "screen A"
    Screen:
        name: "screen E"
        BoxLayout:
            padding:12
            spacing:3
            orientation: 'vertical'
            Button:
                text: "Conditions"
                font_size : 20
                size_hint: (1, 0.1)
            Button:
                background_normal: 'imageE.png'
                background_down: 'down.png'
                size_hint: (1, .8)
                pos_hint: {"center_x": 0.5,"center_y": 0.5}
            Button:
                text: "Retour"
                font_size : 19
                size_hint: (1, 0.1)
                on_release:
                    root.current = "screen A"
    Screen:
        name: "screen F"
        BoxLayout:
            padding:12
            spacing:3
            orientation: 'vertical'
            Button:
                text: "Conditions"
                font_size : 20
                size_hint: (1, 0.1)
            Button:
                background_normal: 'imageF.png'
                background_down: 'down.png'
                size_hint: (1, .8)
                pos_hint: {"center_x": 0.5,"center_y": 0.5}
            Button:
                text: "Retour"
                font_size : 19
                size_hint: (1, 0.1)
                on_release:
                    root.current = "screen A"
    Screen:
        name: "screen G"
        BoxLayout:
            orientation: 'vertical'
            padding:10
            spacing:10
            Button:
                text: "Page Web : Python version arabe"
                font_size : 20
                size_hint: (1, 0.35)
            Button:
                text: "Cliquer Ici"
                font_size : 19
                size_hint: (1, 0.1)
                on_release:
                    app.launch_link(0)
            Button:
                text: "Livre : Introduction pratique à python"
                font_size : 20
                size_hint: (1, 0.35)
            Button:
                text: "Cliquer Ici"
                font_size : 19
                size_hint: (1, 0.1)
                on_release:
                    app.launch_link(1)
            Button:
                text: "Retour"
                font_size : 19
                size_hint: (1, 0.1)
                on_release:
                    root.current = "screen A"      

'''

class Test(App):
    def build(self):
        return Builder.load_string(KV)
Test().run()
