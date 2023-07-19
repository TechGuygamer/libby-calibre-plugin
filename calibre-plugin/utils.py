from collections import namedtuple
from enum import Enum

from calibre.gui2 import is_dark_theme


class PluginColors(str, Enum):
    Red = "#FF0F00" if is_dark_theme() else "#E70E00"
    Green = "#00D228" if is_dark_theme() else "#00BA28"
    Blue = "#6EA8FE" if is_dark_theme() else "#0E6EFD"
    Purple = "#C0A4FF" if is_dark_theme() else "#7B47D1"
    Turquoise = "#07CAF0" if is_dark_theme() else "#07B0D3"
    Gray = "#cccccc" if is_dark_theme() else "#333333"

    def __str__(self):
        return str(self.value)


class PluginIcons(str, Enum):
    Return = "return"
    Download = "download"
    ExternalLink = "ext-link"
    Refresh = "refresh"
    Add = "add-file"
    Delete = "delete"
    AddMagazine = "magazines-add"
    CancelMagazine = "cancel-sub"
    Edit = "pencil-line"
    Cancel = "cancel"
    Okay = "okay"

    def __str__(self):
        return str(self.value)


IconDefinition = namedtuple("IconDefinition", ["file", "color"])

ICON_MAP = {
    PluginIcons.Return: IconDefinition(
        file="images/arrow-go-back-line.svg", color=PluginColors.Red
    ),
    PluginIcons.Download: IconDefinition(
        file="images/download-line.svg", color=PluginColors.Blue
    ),
    PluginIcons.ExternalLink: IconDefinition(
        file="images/external-link-line.svg", color=PluginColors.Purple
    ),
    PluginIcons.Refresh: IconDefinition(
        file="images/refresh-line.svg",
        color="#FFC107" if is_dark_theme() else "#FD7E14",
    ),
    PluginIcons.Add: IconDefinition(
        file="images/file-add-line.svg", color=PluginColors.Blue
    ),
    PluginIcons.Delete: IconDefinition(
        file="images/delete-bin-line.svg", color=PluginColors.Red
    ),
    PluginIcons.AddMagazine: IconDefinition(
        file="images/heart-add-line.svg",
        color="#EA868E" if is_dark_theme() else "#D63284",
    ),
    PluginIcons.CancelMagazine: IconDefinition(
        file="images/dislike-line.svg", color=PluginColors.Red
    ),
    PluginIcons.Edit: IconDefinition(
        file="images/pencil-line.svg", color=PluginColors.Turquoise
    ),
    PluginIcons.Cancel: IconDefinition(
        file="images/close-line.svg", color=PluginColors.Gray
    ),
    PluginIcons.Okay: IconDefinition(
        file="images/check-line.svg", color=PluginColors.Green
    ),
}