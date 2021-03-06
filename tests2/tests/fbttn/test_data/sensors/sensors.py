# ",/usr/bin/env python,
# ,
# Copyright 2018-present Facebook. All Rights Reserved.,
# ,
# This program file is free software; you can redistribute it and/or modify it,
# under the terms of the GNU General Public License as published by the,
# Free Software Foundation; version 2 of the License.,
# ,
# This program is distributed in the hope that it will be useful, but WITHOUT,
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or,
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License,
# for more details.,
# ,
# You should have received a copy of the GNU General Public License,
# along with this program in a file named COPYING; if not, write to the,
# Free Software Foundation, Inc.,,
# 51 Franklin Street, Fifth Floor,,
# Boston, MA 02110-1301 USA,
# ,

SENSORS_SERVER = [
    "MB Outlet Temp",
    "VCCIN VR Temp",
    "VCCGBE VR Temp",
    "1V05PCH VR Temp",
    "SOC Temp",
    "MB Inlet Temp",
    "PCH Temp",
    "SOC Therm Margin",
    "VDDR VR Temp",
    "VCCGBE VR Curr",
    "1V05PCH VR Curr",
    "VCCIN VR Pout",
    "VCCIN VR Curr",
    "VCCIN VR Vol",
    "INA230 Power",
    "INA230 Voltage",
    "SOC Package Pwr",
    "SOC Tjmax",
    "VDDR VR Pout",
    "VDDR VR Curr",
    "VDDR VR Vol",
    "VCCSCSUS VR Curr",
    "VCCSCSUS VR Vol",
    "VCCSCSUS VR Temp",
    "VCCSCSUS VR Pout",
    "VCCGBE VR Pout",
    "VCCGBE VR Vol",
    "1V05PCH VR Pout",
    "1V05PCH VR Vol",
    "SOC DIMMA0 Temp",
    "SOC DIMMA1 Temp",
    "SOC DIMMB0 Temp",
    "SOC DIMMB1 Temp",
    "P3V3_MB",
    "P12V_MB",
    "P1V05_PCH",
    "P3V3_STBY_MB",
    "P5V_STBY_MB",
    "PV_BAT",
    "PVDDR",
    "PVCCGBE",
]


SENSORS_IOM = [
    "ML_SENSOR_HSC_VOLT",
    "ML_SENSOR_HSC_CURR",
    "ML_SENSOR_HSC_PWR",
    "IOM_NIC_Ambient_Temp",
    "IOM_HSC_POWER",
    "IOM_HSC_VOLT",
    "IOM_HSC_CURR",
    "ADC_12V",
    "ADC_P5V_STBY",
    "ADC_P3V3_STBY",
    "ADC_P1V8_STBY",
    "ADC_P2V5_STBY",
    "ADC_P1V2_STBY",
    "ADC_P1V15_STBY",
    "ADC_P3V3",
    "ADC_P3V3_M2",
    "M2_Ambient_Temp_1",
    "M2_Ambient_Temp_2",
    "M2_SMART_Temp_1",
    "M2_SMART_Temp_2",
]

SENSORS_DPB = [
    "P3V3_SENSE",
    "P5V_1_SENSE",
    "P5V_2_SENSE",
    "P5V_3_SENSE",
    "P5V_4_SENSE",
    "DPB_12V_POWER_CLIP",
    "DPB_P12V_CLIP",
    "DPB_12V_CURR_CLIP",
    "DPB_Inlet_Temp_1",
    "DPB_Inlet_Temp_2",
    "FAN1_FRONT",
    "FAN1_REAR",
    "FAN2_FRONT",
    "FAN2_REAR",
    "FAN3_FRONT",
    "FAN3_REAR",
    "FAN4_FRONT",
    "FAN4_REAR",
    "DPB_HSC_POWER",
    "DPB_HSC_VOLT",
    "DPB_HSC_CURR",
    "HDD_0_TEMP",
    "HDD_1_TEMP",
    "HDD_2_TEMP",
    "HDD_3_TEMP",
    "HDD_4_TEMP",
    "HDD_5_TEMP",
    "HDD_6_TEMP",
    "HDD_7_TEMP",
    "HDD_8_TEMP",
    "HDD_9_TEMP",
    "HDD_10_TEMP",
    "HDD_11_TEMP",
    "HDD_12_TEMP",
    "HDD_13_TEMP",
    "HDD_14_TEMP",
    "HDD_15_TEMP",
    "HDD_16_TEMP",
    "HDD_17_TEMP",
    "HDD_18_TEMP",
    "HDD_19_TEMP",
    "HDD_20_TEMP",
    "HDD_21_TEMP",
    "HDD_22_TEMP",
    "HDD_23_TEMP",
    "HDD_24_TEMP",
    "HDD_25_TEMP",
    "HDD_26_TEMP",
    "HDD_27_TEMP",
    "HDD_28_TEMP",
    "HDD_29_TEMP",
    "HDD_30_TEMP",
    "HDD_31_TEMP",
    "HDD_32_TEMP",
    "HDD_33_TEMP",
    "HDD_34_TEMP",
    "HDD_35_TEMP",
    "Airflow",
]

SENSORS_SCC = [
    "EXPANDER_TEMP",
    "IOC_TEMP",
    "SCC_HSC_POWER",
    "SCC_HSC_CURR",
    "SCC_HSC_VOLT",
    "P3V3_SENSE",
    "P1V8_E_SENSE",
    "P1V5_E_SENSE",
    "P0V9_SENSE",
    "P1V8_C_SENSE",
    "P1V5_C_SENSE",
    "P0V975_SENSE",
]

SENSORS_MEZZ = ["MEZZ_SENSOR_TEMP"]

SENSORS = {
    "server": SENSORS_SERVER,
    "iom": SENSORS_IOM,
    "dpb": SENSORS_DPB,
    "scc": SENSORS_SCC,
    "nic": SENSORS_MEZZ,
}
