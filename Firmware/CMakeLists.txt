cmake_minimum_required(VERSION 3.0.2)
project(opq.elf)

INCLUDE(CMakeForceCompiler)

SET(CMAKE_SYSTEM_NAME Generic)
SET(CMAKE_SYSTEM_VERSION 1)

# specify the cross compiler
CMAKE_FORCE_C_COMPILER(arm-none-eabi-gcc GNU)
CMAKE_FORCE_CXX_COMPILER(arm-none-eabi-g++ GNU)

SET(COMMON_FLAGS "-mcpu=cortex-m4 \
        -mthumb \
       -mfpu=fpv4-sp-d16 \
       -mfloat-abi=hard \
       -DSTM32F303VC -DSTM32F30X \
        -D__FPU_USED \
        -DUSE_STDPERIPH_DRIVER \
        -I${PROJECT_SOURCE_DIR}/src/cmsis_boot/headers/ \
        -I${PROJECT_SOURCE_DIR}/src/cmsis/headers/ \
        -I${PROJECT_SOURCE_DIR}/src/stm_lib/headers/    \
        -I${PROJECT_SOURCE_DIR}/src/opq/    \
        ")
SET(CMAKE_CXX_FLAGS ${COMMON_FLAGS})
SET(CMAKE_C_FLAGS ${COMMON_FLAGS})
SET(CMAKE_C_LINK_FLAGS "-Wl,-gc-sections,-T${PROJECT_SOURCE_DIR}/src/arm-gcc-link.ld")
SET(CMAKE_SHARED_LIBRARY_LINK_C_FLAGS "-Wl,-gc-sections,-T${PROJECT_SOURCE_DIR}/src/arm-gcc-link.ld")

INCLUDE_DIRECTORIES("${PROJECT_SOURCE_DIR}/src/cmsis_boot/headers/ \
    ${PROJECT_SOURCE_DIR}/src/cmsis/headers/ \
    ${PROJECT_SOURCE_DIR}/src/stm_lib/headers/ \
    ${PROJECT_SOURCE_DIR}/src/opq/ \
    ")

set(HEADER_FILES
        src/cmsis/headers/arm_common_tables.h
        src/cmsis/headers/arm_math.h
        src/cmsis/headers/core_cm0.h
        src/cmsis/headers/core_cm4.h
        src/cmsis/headers/core_cm4_simd.h
        src/cmsis/headers/core_cmFunc.h
        src/cmsis/headers/core_cmInstr.h
        src/cmsis/headers/core_sc000.h
        src/cmsis/headers/core_sc300.h
        src/cmsis_boot/headers/stm32f30x.h
        src/cmsis_boot/headers/stm32f30x_conf.h
        src/cmsis_boot/headers/system_stm32f30x.h
        src/opq/c/config.h
        src/opq/c/datastructures.h
        src/opq/c/main.h
        src/opq/c/platform_config.h
        src/opq/c/stm32f30x_it.h
        src/stm_lib/headers/stm32f30x_adc.h
        src/stm_lib/headers/stm32f30x_can.h
        src/stm_lib/headers/stm32f30x_comp.h
        src/stm_lib/headers/stm32f30x_crc.h
        src/stm_lib/headers/stm32f30x_dac.h
        src/stm_lib/headers/stm32f30x_dbgmcu.h
        src/stm_lib/headers/stm32f30x_dma.h
        src/stm_lib/headers/stm32f30x_exti.h
        src/stm_lib/headers/stm32f30x_flash.h
        src/stm_lib/headers/stm32f30x_gpio.h
        src/stm_lib/headers/stm32f30x_i2c.h
        src/stm_lib/headers/stm32f30x_iwdg.h
        src/stm_lib/headers/stm32f30x_misc.h
        src/stm_lib/headers/stm32f30x_opamp.h
        src/stm_lib/headers/stm32f30x_pwr.h
        src/stm_lib/headers/stm32f30x_rcc.h
        src/stm_lib/headers/stm32f30x_rtc.h
        src/stm_lib/headers/stm32f30x_spi.h
        src/stm_lib/headers/stm32f30x_syscfg.h
        src/stm_lib/headers/stm32f30x_tim.h
        src/stm_lib/headers/stm32f30x_usart.h
        src/stm_lib/headers/stm32f30x_wwdg.h
        )

set(SOURCE_FILES
    src/cmsis_boot/c/startup_stm32f303.c
    src/cmsis_boot/c/system_stm32f30x.c
    src/opq/c/config.c
    src/opq/c/main.c
    src/opq/c/stm32f30x_it.c
    src/stm_lib/c/stm32f30x_adc.c
    src/stm_lib/c/stm32f30x_can.c
    src/stm_lib/c/stm32f30x_comp.c
    src/stm_lib/c/stm32f30x_crc.c
    src/stm_lib/c/stm32f30x_dac.c
    src/stm_lib/c/stm32f30x_dbgmcu.c
    src/stm_lib/c/stm32f30x_dma.c
    src/stm_lib/c/stm32f30x_exti.c
    src/stm_lib/c/stm32f30x_flash.c
    src/stm_lib/c/stm32f30x_gpio.c
    src/stm_lib/c/stm32f30x_i2c.c
    src/stm_lib/c/stm32f30x_iwdg.c
    src/stm_lib/c/stm32f30x_misc.c
    src/stm_lib/c/stm32f30x_opamp.c
    src/stm_lib/c/stm32f30x_pwr.c
    src/stm_lib/c/stm32f30x_rcc.c
    src/stm_lib/c/stm32f30x_rtc.c
    src/stm_lib/c/stm32f30x_spi.c
    src/stm_lib/c/stm32f30x_syscfg.c
    src/stm_lib/c/stm32f30x_tim.c
    src/stm_lib/c/stm32f30x_usart.c
    src/stm_lib/c/stm32f30x_wwdg.c
)

add_executable(opq.elf
        ${SOURCE_FILES}
        ${HEADER_FILES})