"""Unit tests _helper module."""
import unittest

from pyvlx import (
    Blade, Blind, GarageDoor, Gate, Light, PyVLX, RollerShutter, Window)
from pyvlx.api.frames import FrameGetNodeInformationNotification
from pyvlx.const import NodeTypeWithSubtype
from pyvlx.node_helper import convert_frame_to_node


class TestNodeHelper(unittest.TestCase):
    """Test class for helper functions of node_helper."""

    # pylint: disable=too-many-public-methods,invalid-name

    def test_window(self):
        """Test convert_frame_to_node with window."""
        frame = FrameGetNodeInformationNotification()
        frame.node_id = 23
        frame.name = "Fnord23"
        frame.node_type = NodeTypeWithSubtype.WINDOW_OPENER
        frame.serial_number = "aa:bb:aa:bb:aa:bb:aa:23"
        pyvlx = PyVLX()
        node = convert_frame_to_node(pyvlx, frame)
        self.assertEqual(
            node,
            Window(
                pyvlx=pyvlx,
                name="Fnord23",
                node_id=23,
                serial_number="aa:bb:aa:bb:aa:bb:aa:23",
            ),
        )

    def test_window_with_rain_sensor(self):
        """Test convert_frame_to_node with window with rain sensor."""
        frame = FrameGetNodeInformationNotification()
        frame.node_id = 23
        frame.name = "Fnord23"
        frame.node_type = NodeTypeWithSubtype.WINDOW_OPENER_WITH_RAIN_SENSOR
        frame.serial_number = "aa:bb:aa:bb:aa:bb:aa:23"
        pyvlx = PyVLX()
        node = convert_frame_to_node(pyvlx, frame)
        self.assertEqual(
            node,
            Window(
                pyvlx=pyvlx,
                name="Fnord23",
                node_id=23,
                rain_sensor=True,
                serial_number="aa:bb:aa:bb:aa:bb:aa:23",
            ),
        )

    def test_blind(self):
        """Test convert_frame_to_node with blind."""
        frame = FrameGetNodeInformationNotification()
        frame.node_id = 23
        frame.name = "Fnord23"
        frame.node_type = NodeTypeWithSubtype.EXTERIOR_VENETIAN_BLIND
        frame.serial_number = "aa:bb:aa:bb:aa:bb:aa:23"
        pyvlx = PyVLX()
        node = convert_frame_to_node(pyvlx, frame)
        self.assertEqual(
            node,
            Blind(
                pyvlx=pyvlx,
                name="Fnord23",
                node_id=23,
                serial_number="aa:bb:aa:bb:aa:bb:aa:23",
            ),
        )

    def test_roller_shutter(self):
        """Test convert_frame_to_node roller shutter."""
        frame = FrameGetNodeInformationNotification()
        frame.node_id = 23
        frame.name = "Fnord23"
        frame.node_type = NodeTypeWithSubtype.ROLLER_SHUTTER
        frame.serial_number = "aa:bb:aa:bb:aa:bb:aa:23"
        pyvlx = PyVLX()
        node = convert_frame_to_node(pyvlx, frame)
        self.assertEqual(
            node,
            RollerShutter(
                pyvlx=pyvlx,
                name="Fnord23",
                node_id=23,
                serial_number="aa:bb:aa:bb:aa:bb:aa:23",
            ),
        )

    def test_garage_door(self):
        """Test convert_frame_to_node garage door."""
        frame = FrameGetNodeInformationNotification()
        frame.node_id = 23
        frame.name = "Fnord23"
        frame.node_type = NodeTypeWithSubtype.GARAGE_DOOR_OPENER
        frame.serial_number = "aa:bb:aa:bb:aa:bb:aa:23"
        pyvlx = PyVLX()
        node = convert_frame_to_node(pyvlx, frame)
        self.assertEqual(
            node,
            GarageDoor(
                pyvlx=pyvlx,
                name="Fnord23",
                node_id=23,
                serial_number="aa:bb:aa:bb:aa:bb:aa:23",
            ),
        )

    def test_linar_angular_position_of_garage_door(self):
        """Test convert_frame_to_node linar angular position of garage door."""
        frame = FrameGetNodeInformationNotification()
        frame.node_id = 23
        frame.name = "Fnord23"
        frame.node_type = NodeTypeWithSubtype.LINAR_ANGULAR_POSITION_OF_GARAGE_DOOR
        frame.serial_number = "aa:bb:aa:bb:aa:bb:aa:23"
        pyvlx = PyVLX()
        node = convert_frame_to_node(pyvlx, frame)
        self.assertEqual(
            node,
            GarageDoor(
                pyvlx=pyvlx,
                name="Fnord23",
                node_id=23,
                serial_number="aa:bb:aa:bb:aa:bb:aa:23",
            ),
        )

    def test_gate(self):
        """Test convert_frame_to_node gate."""
        frame = FrameGetNodeInformationNotification()
        frame.node_id = 23
        frame.name = "Fnord23"
        frame.node_type = NodeTypeWithSubtype.GATE_OPENER
        frame.serial_number = "aa:bb:aa:bb:aa:bb:aa:23"
        pyvlx = PyVLX()
        node = convert_frame_to_node(pyvlx, frame)
        self.assertEqual(
            node,
            Gate(
                pyvlx=pyvlx,
                name="Fnord23",
                node_id=23,
                serial_number="aa:bb:aa:bb:aa:bb:aa:23",
            ),
        )

    def test_gate_with_angular_position(self):
        """Test convert_frame_to_node gate."""
        frame = FrameGetNodeInformationNotification()
        frame.node_id = 23
        frame.name = "Fnord23"
        frame.node_type = NodeTypeWithSubtype.GATE_OPENER_ANGULAR_POSITION
        frame.serial_number = "aa:bb:aa:bb:aa:bb:aa:23"
        pyvlx = PyVLX()
        node = convert_frame_to_node(pyvlx, frame)
        self.assertEqual(
            node,
            Gate(
                pyvlx=pyvlx,
                name="Fnord23",
                node_id=23,
                serial_number="aa:bb:aa:bb:aa:bb:aa:23",
            ),
        )

    def test_blade(self):
        """Test convert_frame_to_node blade."""
        frame = FrameGetNodeInformationNotification()
        frame.node_id = 23
        frame.name = "Fnord23"
        frame.node_type = NodeTypeWithSubtype.BLADE_OPENER
        frame.serial_number = "aa:bb:aa:bb:aa:bb:aa:23"
        pyvlx = PyVLX()
        node = convert_frame_to_node(pyvlx, frame)
        self.assertEqual(
            node,
            Blade(
                pyvlx=pyvlx,
                name="Fnord23",
                node_id=23,
                serial_number="aa:bb:aa:bb:aa:bb:aa:23",
            ),
        )

    def test_no_type(self):
        """Test convert_frame_to_node with no type (convert_frame_to_node should return None)."""
        frame = FrameGetNodeInformationNotification()
        frame.node_id = 23
        frame.name = "Fnord23"
        frame.node_type = NodeTypeWithSubtype.NO_TYPE
        frame.serial_number = "aa:bb:aa:bb:aa:bb:aa:23"
        pyvlx = PyVLX()
        self.assertEqual(convert_frame_to_node(pyvlx, frame), None)

    def test_light(self):
        """Test convert_frame_to_node with light."""
        frame = FrameGetNodeInformationNotification()
        frame.node_id = 23
        frame.name = "Fnord23"
        frame.node_type = NodeTypeWithSubtype.LIGHT
        frame.serial_number = "aa:bb:aa:bb:aa:bb:aa:23"
        pyvlx = PyVLX()
        node = convert_frame_to_node(pyvlx, frame)
        self.assertEqual(
            node,
            Light(
                pyvlx=pyvlx,
                name="Fnord23",
                node_id=23,
                serial_number="aa:bb:aa:bb:aa:bb:aa:23",
            ),
        )

    def test_light_on_off(self):
        """Test convert_frame_to_node with light_on_off."""
        frame = FrameGetNodeInformationNotification()
        frame.node_id = 23
        frame.name = "Fnord23"
        frame.node_type = NodeTypeWithSubtype.LIGHT_ON_OFF
        frame.serial_number = "aa:bb:aa:bb:aa:bb:aa:23"
        pyvlx = PyVLX()
        node = convert_frame_to_node(pyvlx, frame)
        self.assertEqual(
            node,
            Light(
                pyvlx=pyvlx,
                name="Fnord23",
                node_id=23,
                serial_number="aa:bb:aa:bb:aa:bb:aa:23",
            ),
        )
