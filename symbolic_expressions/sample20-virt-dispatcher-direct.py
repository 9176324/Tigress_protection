#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_15231 = ref_278 # MOV operation
ref_15367 = ref_15231 # MOV operation
ref_15373 = (0x1F02C962 | ref_15367) # OR operation
ref_15534 = ref_15373 # MOV operation
ref_15540 = (0x1F8797B2 & ref_15534) # AND operation
ref_15617 = ref_15540 # MOV operation
ref_16792 = ref_278 # MOV operation
ref_17434 = ref_15617 # MOV operation
ref_17486 = ref_16792 # MOV operation
ref_17490 = ref_17434 # MOV operation
ref_17492 = (ref_17490 & ref_17486) # AND operation
ref_17569 = ref_17492 # MOV operation
ref_18744 = ref_278 # MOV operation
ref_18880 = ref_18744 # MOV operation
ref_18886 = (((sx(0x40, 0x66AF1DF) * sx(0x40, ref_18880)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_19634 = ref_17569 # MOV operation
ref_19678 = ref_19634 # MOV operation
ref_19692 = (ref_19678 >> (0x7 & 0x3F)) # SHR operation
ref_20443 = ref_17569 # MOV operation
ref_20487 = ref_20443 # MOV operation
ref_20501 = ((ref_20487 << (0x39 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_20578 = ref_19692 # MOV operation
ref_20582 = ref_20501 # MOV operation
ref_20584 = (ref_20582 | ref_20578) # OR operation
ref_20661 = ref_18886 # MOV operation
ref_20665 = ref_20584 # MOV operation
ref_20667 = ((ref_20665 + ref_20661) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_20745 = ref_20667 # MOV operation
ref_27429 = ref_20745 # MOV operation
ref_28295 = ref_20745 # MOV operation
ref_28347 = ref_27429 # MOV operation
ref_28351 = ref_28295 # MOV operation
ref_28353 = ((ref_28351 + ref_28347) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_28431 = ref_28353 # MOV operation
ref_30139 = ref_20745 # MOV operation
ref_30921 = ref_17569 # MOV operation
ref_31057 = ref_30921 # MOV operation
ref_31063 = (0x7 & ref_31057) # AND operation
ref_31132 = ref_31063 # MOV operation
ref_31146 = ((ref_31132 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_31223 = ref_30139 # MOV operation
ref_31227 = ref_31146 # MOV operation
ref_31229 = (ref_31227 | ref_31223) # OR operation
ref_31306 = ref_31229 # MOV operation
ref_31308 = ((ref_31306 >> 56) & 0xFF) # Byte reference - MOV operation
ref_31309 = ((ref_31306 >> 48) & 0xFF) # Byte reference - MOV operation
ref_31310 = ((ref_31306 >> 40) & 0xFF) # Byte reference - MOV operation
ref_31311 = ((ref_31306 >> 32) & 0xFF) # Byte reference - MOV operation
ref_31312 = ((ref_31306 >> 24) & 0xFF) # Byte reference - MOV operation
ref_31313 = ((ref_31306 >> 16) & 0xFF) # Byte reference - MOV operation
ref_31314 = ((ref_31306 >> 8) & 0xFF) # Byte reference - MOV operation
ref_31315 = (ref_31306 & 0xFF) # Byte reference - MOV operation
ref_32702 = ref_31308 # MOVZX operation
ref_32746 = (ref_32702 & 0xFF) # MOVZX operation
ref_35274 = ref_31315 # MOVZX operation
ref_35318 = (ref_35274 & 0xFF) # MOVZX operation
ref_35320 = (ref_35318 & 0xFF) # Byte reference - MOV operation
ref_36706 = (ref_32746 & 0xFF) # MOVZX operation
ref_36750 = (ref_36706 & 0xFF) # MOVZX operation
ref_36752 = (ref_36750 & 0xFF) # Byte reference - MOV operation
ref_38002 = ref_15617 # MOV operation
ref_38952 = ((((((((ref_35320) << 8 | ref_31309) << 8 | ref_31310) << 8 | ref_31311) << 8 | ref_31312) << 8 | ref_31313) << 8 | ref_31314) << 8 | ref_36752) # MOV operation
ref_39650 = ref_17569 # MOV operation
ref_39702 = ref_38952 # MOV operation
ref_39706 = ref_39650 # MOV operation
ref_39708 = (ref_39706 & ref_39702) # AND operation
ref_39869 = ref_39708 # MOV operation
ref_39875 = (0x1F & ref_39869) # AND operation
ref_39944 = ref_39875 # MOV operation
ref_39958 = ((ref_39944 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_40035 = ref_38002 # MOV operation
ref_40039 = ref_39958 # MOV operation
ref_40041 = (ref_40039 | ref_40035) # OR operation
ref_40118 = ref_40041 # MOV operation
ref_42537 = ref_28431 # MOV operation
ref_43403 = ref_28431 # MOV operation
ref_43455 = ref_42537 # MOV operation
ref_43459 = ref_43403 # MOV operation
ref_43461 = ((ref_43459 + ref_43455) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_43539 = ref_43461 # MOV operation
ref_45247 = ref_43539 # MOV operation
ref_46029 = ((((((((ref_35320) << 8 | ref_31309) << 8 | ref_31310) << 8 | ref_31311) << 8 | ref_31312) << 8 | ref_31313) << 8 | ref_31314) << 8 | ref_36752) # MOV operation
ref_46165 = ref_46029 # MOV operation
ref_46171 = (0x7 & ref_46165) # AND operation
ref_46240 = ref_46171 # MOV operation
ref_46254 = ((ref_46240 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_46331 = ref_45247 # MOV operation
ref_46335 = ref_46254 # MOV operation
ref_46337 = (ref_46335 | ref_46331) # OR operation
ref_46414 = ref_46337 # MOV operation
ref_46416 = ((ref_46414 >> 56) & 0xFF) # Byte reference - MOV operation
ref_46417 = ((ref_46414 >> 48) & 0xFF) # Byte reference - MOV operation
ref_46418 = ((ref_46414 >> 40) & 0xFF) # Byte reference - MOV operation
ref_46419 = ((ref_46414 >> 32) & 0xFF) # Byte reference - MOV operation
ref_46420 = ((ref_46414 >> 24) & 0xFF) # Byte reference - MOV operation
ref_46421 = ((ref_46414 >> 16) & 0xFF) # Byte reference - MOV operation
ref_46422 = ((ref_46414 >> 8) & 0xFF) # Byte reference - MOV operation
ref_46423 = (ref_46414 & 0xFF) # Byte reference - MOV operation
ref_47810 = ref_46416 # MOVZX operation
ref_47854 = (ref_47810 & 0xFF) # MOVZX operation
ref_50382 = ref_46423 # MOVZX operation
ref_50426 = (ref_50382 & 0xFF) # MOVZX operation
ref_50428 = (ref_50426 & 0xFF) # Byte reference - MOV operation
ref_51814 = (ref_47854 & 0xFF) # MOVZX operation
ref_51858 = (ref_51814 & 0xFF) # MOVZX operation
ref_51860 = (ref_51858 & 0xFF) # Byte reference - MOV operation
ref_53110 = ref_40118 # MOV operation
ref_54060 = ((((((((ref_50428) << 8 | ref_46417) << 8 | ref_46418) << 8 | ref_46419) << 8 | ref_46420) << 8 | ref_46421) << 8 | ref_46422) << 8 | ref_51860) # MOV operation
ref_54758 = ((((((((ref_35320) << 8 | ref_31309) << 8 | ref_31310) << 8 | ref_31311) << 8 | ref_31312) << 8 | ref_31313) << 8 | ref_31314) << 8 | ref_36752) # MOV operation
ref_54810 = ref_54060 # MOV operation
ref_54814 = ref_54758 # MOV operation
ref_54816 = (ref_54814 & ref_54810) # AND operation
ref_54977 = ref_54816 # MOV operation
ref_54983 = (0x1F & ref_54977) # AND operation
ref_55052 = ref_54983 # MOV operation
ref_55066 = ((ref_55052 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_55143 = ref_53110 # MOV operation
ref_55147 = ref_55066 # MOV operation
ref_55149 = (ref_55147 | ref_55143) # OR operation
ref_55226 = ref_55149 # MOV operation
ref_57449 = ((((((((ref_35320) << 8 | ref_31309) << 8 | ref_31310) << 8 | ref_31311) << 8 | ref_31312) << 8 | ref_31313) << 8 | ref_31314) << 8 | ref_36752) # MOV operation
ref_58091 = ((((((((ref_50428) << 8 | ref_46417) << 8 | ref_46418) << 8 | ref_46419) << 8 | ref_46420) << 8 | ref_46421) << 8 | ref_46422) << 8 | ref_51860) # MOV operation
ref_58143 = ref_57449 # MOV operation
ref_58147 = ref_58091 # MOV operation
ref_58149 = (ref_58147 | ref_58143) # OR operation
ref_58310 = ref_58149 # MOV operation
ref_58316 = (0xF & ref_58310) # AND operation
ref_58477 = ref_58316 # MOV operation
ref_58483 = (0x1 | ref_58477) # OR operation
ref_59234 = ref_17569 # MOV operation
ref_59278 = ref_59234 # MOV operation
ref_59292 = (ref_59278 >> (0x1 & 0x3F)) # SHR operation
ref_59453 = ref_59292 # MOV operation
ref_59459 = (0xF & ref_59453) # AND operation
ref_59620 = ref_59459 # MOV operation
ref_59626 = (0x1 | ref_59620) # OR operation
ref_60293 = ref_55226 # MOV operation
ref_60337 = ref_60293 # MOV operation
ref_60349 = ref_59626 # MOV operation
ref_60351 = (ref_60337 >> ((ref_60349 & 0xFF) & 0x3F)) # SHR operation
ref_61102 = ref_17569 # MOV operation
ref_61146 = ref_61102 # MOV operation
ref_61160 = (ref_61146 >> (0x1 & 0x3F)) # SHR operation
ref_61321 = ref_61160 # MOV operation
ref_61327 = (0xF & ref_61321) # AND operation
ref_61488 = ref_61327 # MOV operation
ref_61494 = (0x1 | ref_61488) # OR operation
ref_61659 = ref_61494 # MOV operation
ref_61661 = ((0x40 - ref_61659) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_61669 = ref_61661 # MOV operation
ref_62331 = ref_55226 # MOV operation
ref_62375 = ref_62331 # MOV operation
ref_62387 = ref_61669 # MOV operation
ref_62389 = ((ref_62375 << ((ref_62387 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_62466 = ref_60351 # MOV operation
ref_62470 = ref_62389 # MOV operation
ref_62472 = (ref_62470 | ref_62466) # OR operation
ref_62541 = ref_62472 # MOV operation
ref_62553 = ref_58483 # MOV operation
ref_62555 = ((ref_62541 << ((ref_62553 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_63222 = ((((((((ref_35320) << 8 | ref_31309) << 8 | ref_31310) << 8 | ref_31311) << 8 | ref_31312) << 8 | ref_31313) << 8 | ref_31314) << 8 | ref_36752) # MOV operation
ref_63864 = ((((((((ref_50428) << 8 | ref_46417) << 8 | ref_46418) << 8 | ref_46419) << 8 | ref_46420) << 8 | ref_46421) << 8 | ref_46422) << 8 | ref_51860) # MOV operation
ref_63916 = ref_63222 # MOV operation
ref_63920 = ref_63864 # MOV operation
ref_63922 = (ref_63920 | ref_63916) # OR operation
ref_64083 = ref_63922 # MOV operation
ref_64089 = (0xF & ref_64083) # AND operation
ref_64250 = ref_64089 # MOV operation
ref_64256 = (0x1 | ref_64250) # OR operation
ref_64421 = ref_64256 # MOV operation
ref_64423 = ((0x40 - ref_64421) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_64431 = ref_64423 # MOV operation
ref_65177 = ref_17569 # MOV operation
ref_65221 = ref_65177 # MOV operation
ref_65235 = (ref_65221 >> (0x1 & 0x3F)) # SHR operation
ref_65396 = ref_65235 # MOV operation
ref_65402 = (0xF & ref_65396) # AND operation
ref_65563 = ref_65402 # MOV operation
ref_65569 = (0x1 | ref_65563) # OR operation
ref_66236 = ref_55226 # MOV operation
ref_66280 = ref_66236 # MOV operation
ref_66292 = ref_65569 # MOV operation
ref_66294 = (ref_66280 >> ((ref_66292 & 0xFF) & 0x3F)) # SHR operation
ref_67045 = ref_17569 # MOV operation
ref_67089 = ref_67045 # MOV operation
ref_67103 = (ref_67089 >> (0x1 & 0x3F)) # SHR operation
ref_67264 = ref_67103 # MOV operation
ref_67270 = (0xF & ref_67264) # AND operation
ref_67431 = ref_67270 # MOV operation
ref_67437 = (0x1 | ref_67431) # OR operation
ref_67602 = ref_67437 # MOV operation
ref_67604 = ((0x40 - ref_67602) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_67612 = ref_67604 # MOV operation
ref_68274 = ref_55226 # MOV operation
ref_68318 = ref_68274 # MOV operation
ref_68330 = ref_67612 # MOV operation
ref_68332 = ((ref_68318 << ((ref_68330 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_68409 = ref_66294 # MOV operation
ref_68413 = ref_68332 # MOV operation
ref_68415 = (ref_68413 | ref_68409) # OR operation
ref_68484 = ref_68415 # MOV operation
ref_68496 = ref_64431 # MOV operation
ref_68498 = (ref_68484 >> ((ref_68496 & 0xFF) & 0x3F)) # SHR operation
ref_68575 = ref_62555 # MOV operation
ref_68579 = ref_68498 # MOV operation
ref_68581 = (ref_68579 | ref_68575) # OR operation
ref_68658 = ref_68581 # MOV operation
ref_68812 = ref_68658 # MOV operation
ref_68814 = ref_68812 # MOV operation

print ref_68814 & 0xffffffffffffffff