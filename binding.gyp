{
    "targets": [{
        "target_name": "lwip",
        "sources": [
            "lwip.cpp",
            "LwipImage.cpp",
            "lib/jpeg/jmemansi.c",
            "lib/jpeg/jaricom.c",
            "lib/jpeg/jcapimin.c",
            "lib/jpeg/jcapistd.c",
            "lib/jpeg/jcarith.c",
            "lib/jpeg/jccoefct.c",
            "lib/jpeg/jccolor.c",
            "lib/jpeg/jcdctmgr.c",
            "lib/jpeg/jchuff.c",
            "lib/jpeg/jcinit.c",
            "lib/jpeg/jcmainct.c",
            "lib/jpeg/jcmarker.c",
            "lib/jpeg/jcmaster.c",
            "lib/jpeg/jcomapi.c",
            "lib/jpeg/jcparam.c",
            "lib/jpeg/jcprepct.c",
            "lib/jpeg/jcsample.c",
            "lib/jpeg/jctrans.c",
            "lib/jpeg/jdapimin.c",
            "lib/jpeg/jdapistd.c",
            "lib/jpeg/jdarith.c",
            "lib/jpeg/jdatadst.c",
            "lib/jpeg/jdatasrc.c",
            "lib/jpeg/jdcoefct.c",
            "lib/jpeg/jdcolor.c",
            "lib/jpeg/jddctmgr.c",
            "lib/jpeg/jdhuff.c",
            "lib/jpeg/jdinput.c",
            "lib/jpeg/jdmainct.c",
            "lib/jpeg/jdmarker.c",
            "lib/jpeg/jdmaster.c",
            "lib/jpeg/jdmerge.c",
            "lib/jpeg/jdpostct.c",
            "lib/jpeg/jdsample.c",
            "lib/jpeg/jdtrans.c",
            "lib/jpeg/jerror.c",
            "lib/jpeg/jfdctflt.c",
            "lib/jpeg/jfdctfst.c",
            "lib/jpeg/jfdctint.c",
            "lib/jpeg/jidctflt.c",
            "lib/jpeg/jidctfst.c",
            "lib/jpeg/jidctint.c",
            "lib/jpeg/jquant1.c",
            "lib/jpeg/jquant2.c",
            "lib/jpeg/jutils.c",
            "lib/jpeg/jmemmgr.c"
        ],
        'cflags!': ['-fno-exceptions'],
        'cflags_cc!': ['-fno-exceptions'],
        'include_dirs': ['lib/jpeg'],
        'conditions': [
            ['OS=="mac"', {
                'xcode_settings': {
                    'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
                },
                'include_dirs': ['/usr/include/malloc']
            }]
        ]
    }]
}