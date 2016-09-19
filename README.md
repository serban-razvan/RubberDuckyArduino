# RubberDuckyArduino

1. Description
2. Usage
3. Wiring

## Description

[Rubber Ducky](http://usbrubberducky.com/#!index.md) is a usb stick that acts as a keyboard, fooling any device not to test its validity. We can use it to send any keyboard commands that we previously stored them into a script.

The device is fairly expensive at the time of writing, so a cheaper alternative is available: using a Arduino with ATmega32u4 processor (Arduino Yun, Arduino Leonardo or the smallest one: [Arduino Micro](https://www.arduino.cc/en/Main/ArduinoBoardMicro)).

## Usage

Take the script written in Rubber Ducky's language ([Examples](https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Payloads)), put it in a file in the same folder as the script.py and then run script.py. Follow the instructions and after finishing, run Arduino program for flashing boards, choosing the board from the menu and the .ino file from this repository.

After flashing, connect the board to the victim's PC and then after pressing on the button (schematics below), the script will run.

## Wiring

![Schematic](http://i.imgur.com/bTy6J5c.png)
