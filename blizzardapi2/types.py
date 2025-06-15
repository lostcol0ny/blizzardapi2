from enum import Enum


class Region(str, Enum):
    """Region enum for Blizzard API endpoints."""

    US = "us"
    EU = "eu"
    KR = "kr"
    TW = "tw"
    CN = "cn"


class Locale(str, Enum):
    """Locale enum for Blizzard API responses."""

    EN_US = "en_US"
    EN_GB = "en_GB"
    ES_ES = "es_ES"
    ES_MX = "es_MX"
    PT_BR = "pt_BR"
    DE_DE = "de_DE"
    FR_FR = "fr_FR"
    IT_IT = "it_IT"
    PL_PL = "pl_PL"
    RU_RU = "ru_RU"
    KO_KR = "ko_KR"
    ZH_TW = "zh_TW"
    ZH_CN = "zh_CN"
