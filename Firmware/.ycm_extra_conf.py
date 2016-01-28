flags = [
  # General flags
  '-Wall'
  ,'-Wextra'
  ,'-Werror'

  ,'-Wno-attributes'
  ,'-std=c++11'
  ,'-x'
  ,'c++'

  ,'-Isrc/cmsis/headers'
  ,'-Isrc/cmsis_boot/headers'
  ,'-Isrc/stm_lib/headers'

  ,'-DF_CPU=16000000L'
  ,'-DARDUINO=163'
  ,'-D__AVR__'
  ,'-D__AVR_ATmega2560__'
]
