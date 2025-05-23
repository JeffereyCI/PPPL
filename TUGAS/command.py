# Command interface
class Command:
   def execute(self):
       pass


# Receiver
class TV:
   def __init__(self):
       self.is_on = False


   def turn_on(self):
       if not self.is_on:
           self.is_on = True
           print("TV Dinyalakan 📺")
       else:
           print("TV sudah menyala")


   def turn_off(self):
       if self.is_on:
           self.is_on = False
           print("TV Dimatikan ❌")
       else:
           print("TV sudah mati")


# ConcreteCommand
class PowerToggleCommand(Command):
   def __init__(self, tv):
       self.tv = tv


   def execute(self):
       if self.tv.is_on:
           self.tv.turn_off()
       else:
           self.tv.turn_on()


# Invoker
class RemoteControl:
   def __init__(self):
       self.command = None


   def set_command(self, command):
       self.command = command


   def press_button(self):
       self.command.execute()


# Client Code
tv = TV()
remote = RemoteControl()


power_command = PowerToggleCommand(tv)
remote.set_command(power_command)


# Tekan tombol power beberapa kali
remote.press_button()  # TV Dinyalakan 📺
remote.press_button()  # TV Dimatikan ❌
remote.press_button()  # TV Dinyalakan 📺