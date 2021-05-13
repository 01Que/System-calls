#!/usr/bin/python3

# Content autogenerated. Do not edit.

syscalls_i386 = {
    "_llseek": 140,
    "_newselect": 142,
    "_sysctl": 149,
    "accept4": 364,
    "access": 33,
    "acct": 51,
    "add_key": 286,
    "adjtimex": 124,
    "alarm": 27,
    "arch_prctl": 384,
    "bdflush": 134,
    "bind": 361,
    "bpf": 357,
    "brk": 45,
    "capget": 184,
    "capset": 185,
    "chdir": 12,
    "chmod": 15,
    "chown": 182,
    "chown32": 212,
    "chroot": 61,
    "clock_adjtime": 343,
    "clock_adjtime64": 405,
    "clock_getres": 266,
    "clock_getres_time64": 406,
    "clock_gettime": 265,
    "clock_gettime64": 403,
    "clock_nanosleep": 267,
    "clock_nanosleep_time64": 407,
    "clock_settime": 264,
    "clock_settime64": 404,
    "clone": 120,
    "clone3": 435,
    "close": 6,
    "close_range": 436,
    "connect": 362,
    "copy_file_range": 377,
    "creat": 8,
    "create_module": 127,
    "delete_module": 129,
    "dup": 41,
    "dup2": 63,
    "dup3": 330,
    "epoll_create": 254,
    "epoll_create1": 329,
    "epoll_ctl": 255,
    "epoll_pwait": 319,
    "epoll_pwait2": 441,
    "epoll_wait": 256,
    "eventfd": 323,
    "eventfd2": 328,
    "execve": 11,
    "execveat": 358,
    "exit": 1,
    "exit_group": 252,
    "faccessat": 307,
    "faccessat2": 439,
    "fadvise64": 250,
    "fadvise64_64": 272,
    "fallocate": 324,
    "fanotify_init": 338,
    "fanotify_mark": 339,
    "fchdir": 133,
    "fchmod": 94,
    "fchmodat": 306,
    "fchown": 95,
    "fchown32": 207,
    "fchownat": 298,
    "fcntl": 55,
    "fcntl64": 221,
    "fdatasync": 148,
    "fgetxattr": 231,
    "finit_module": 350,
    "flistxattr": 234,
    "flock": 143,
    "fork": 2,
    "fremovexattr": 237,
    "fsconfig": 431,
    "fsetxattr": 228,
    "fsmount": 432,
    "fsopen": 430,
    "fspick": 433,
    "fstat": 108,
    "fstat64": 197,
    "fstatat64": 300,
    "fstatfs": 100,
    "fstatfs64": 269,
    "fsync": 118,
    "ftruncate": 93,
    "ftruncate64": 194,
    "futex": 240,
    "futex_time64": 422,
    "futimesat": 299,
    "get_kernel_syms": 130,
    "get_mempolicy": 275,
    "get_robust_list": 312,
    "get_thread_area": 244,
    "getcpu": 318,
    "getcwd": 183,
    "getdents": 141,
    "getdents64": 220,
    "getegid": 50,
    "getegid32": 202,
    "geteuid": 49,
    "geteuid32": 201,
    "getgid": 47,
    "getgid32": 200,
    "getgroups": 80,
    "getgroups32": 205,
    "getitimer": 105,
    "getpeername": 368,
    "getpgid": 132,
    "getpgrp": 65,
    "getpid": 20,
    "getpmsg": 188,
    "getppid": 64,
    "getpriority": 96,
    "getrandom": 355,
    "getresgid": 171,
    "getresgid32": 211,
    "getresuid": 165,
    "getresuid32": 209,
    "getrlimit": 76,
    "getrusage": 77,
    "getsid": 147,
    "getsockname": 367,
    "getsockopt": 365,
    "gettid": 224,
    "gettimeofday": 78,
    "getuid": 24,
    "getuid32": 199,
    "getxattr": 229,
    "idle": 112,
    "init_module": 128,
    "inotify_add_watch": 292,
    "inotify_init": 291,
    "inotify_init1": 332,
    "inotify_rm_watch": 293,
    "io_cancel": 249,
    "io_destroy": 246,
    "io_getevents": 247,
    "io_pgetevents": 385,
    "io_pgetevents_time64": 416,
    "io_setup": 245,
    "io_submit": 248,
    "io_uring_enter": 426,
    "io_uring_register": 427,
    "io_uring_setup": 425,
    "ioctl": 54,
    "ioperm": 101,
    "iopl": 110,
    "ioprio_get": 290,
    "ioprio_set": 289,
    "ipc": 117,
    "kcmp": 349,
    "kexec_load": 283,
    "keyctl": 288,
    "kill": 37,
    "lchown": 16,
    "lchown32": 198,
    "lgetxattr": 230,
    "link": 9,
    "linkat": 303,
    "listen": 363,
    "listxattr": 232,
    "llistxattr": 233,
    "lookup_dcookie": 253,
    "lremovexattr": 236,
    "lseek": 19,
    "lsetxattr": 227,
    "lstat": 107,
    "lstat64": 196,
    "madvise": 219,
    "mbind": 274,
    "membarrier": 375,
    "memfd_create": 356,
    "migrate_pages": 294,
    "mincore": 218,
    "mkdir": 39,
    "mkdirat": 296,
    "mknod": 14,
    "mknodat": 297,
    "mlock": 150,
    "mlock2": 376,
    "mlockall": 152,
    "mmap": 90,
    "mmap2": 192,
    "modify_ldt": 123,
    "mount": 21,
    "mount_setattr": 442,
    "move_mount": 429,
    "move_pages": 317,
    "mprotect": 125,
    "mq_getsetattr": 282,
    "mq_notify": 281,
    "mq_open": 277,
    "mq_timedreceive": 280,
    "mq_timedreceive_time64": 419,
    "mq_timedsend": 279,
    "mq_timedsend_time64": 418,
    "mq_unlink": 278,
    "mremap": 163,
    "msgctl": 402,
    "msgget": 399,
    "msgrcv": 401,
    "msgsnd": 400,
    "msync": 144,
    "munlock": 151,
    "munlockall": 153,
    "munmap": 91,
    "name_to_handle_at": 341,
    "nanosleep": 162,
    "nfsservctl": 169,
    "nice": 34,
    "oldfstat": 28,
    "oldlstat": 84,
    "oldolduname": 59,
    "oldstat": 18,
    "olduname": 109,
    "open": 5,
    "open_by_handle_at": 342,
    "open_tree": 428,
    "openat": 295,
    "openat2": 437,
    "pause": 29,
    "perf_event_open": 336,
    "personality": 136,
    "pidfd_getfd": 438,
    "pidfd_open": 434,
    "pidfd_send_signal": 424,
    "pipe": 42,
    "pipe2": 331,
    "pivot_root": 217,
    "pkey_alloc": 381,
    "pkey_free": 382,
    "pkey_mprotect": 380,
    "poll": 168,
    "ppoll": 309,
    "ppoll_time64": 414,
    "prctl": 172,
    "pread64": 180,
    "preadv": 333,
    "preadv2": 378,
    "prlimit64": 340,
    "process_madvise": 440,
    "process_vm_readv": 347,
    "process_vm_writev": 348,
    "pselect6": 308,
    "pselect6_time64": 413,
    "ptrace": 26,
    "pwrite64": 181,
    "pwritev": 334,
    "pwritev2": 379,
    "query_module": 167,
    "quotactl": 131,
    "quotactl_path": 443,
    "read": 3,
    "readahead": 225,
    "readdir": 89,
    "readlink": 85,
    "readlinkat": 305,
    "readv": 145,
    "reboot": 88,
    "recvfrom": 371,
    "recvmmsg": 337,
    "recvmmsg_time64": 417,
    "recvmsg": 372,
    "remap_file_pages": 257,
    "removexattr": 235,
    "rename": 38,
    "renameat": 302,
    "renameat2": 353,
    "request_key": 287,
    "restart_syscall": 0,
    "rmdir": 40,
    "rseq": 386,
    "rt_sigaction": 174,
    "rt_sigpending": 176,
    "rt_sigprocmask": 175,
    "rt_sigqueueinfo": 178,
    "rt_sigreturn": 173,
    "rt_sigsuspend": 179,
    "rt_sigtimedwait": 177,
    "rt_sigtimedwait_time64": 421,
    "rt_tgsigqueueinfo": 335,
    "sched_get_priority_max": 159,
    "sched_get_priority_min": 160,
    "sched_getaffinity": 242,
    "sched_getattr": 352,
    "sched_getparam": 155,
    "sched_getscheduler": 157,
    "sched_rr_get_interval": 161,
    "sched_rr_get_interval_time64": 423,
    "sched_setaffinity": 241,
    "sched_setattr": 351,
    "sched_setparam": 154,
    "sched_setscheduler": 156,
    "sched_yield": 158,
    "seccomp": 354,
    "select": 82,
    "semctl": 394,
    "semget": 393,
    "semtimedop_time64": 420,
    "sendfile": 187,
    "sendfile64": 239,
    "sendmmsg": 345,
    "sendmsg": 370,
    "sendto": 369,
    "set_mempolicy": 276,
    "set_robust_list": 311,
    "set_thread_area": 243,
    "set_tid_address": 258,
    "setdomainname": 121,
    "setfsgid": 139,
    "setfsgid32": 216,
    "setfsuid": 138,
    "setfsuid32": 215,
    "setgid": 46,
    "setgid32": 214,
    "setgroups": 81,
    "setgroups32": 206,
    "sethostname": 74,
    "setitimer": 104,
    "setns": 346,
    "setpgid": 57,
    "setpriority": 97,
    "setregid": 71,
    "setregid32": 204,
    "setresgid": 170,
    "setresgid32": 210,
    "setresuid": 164,
    "setresuid32": 208,
    "setreuid": 70,
    "setreuid32": 203,
    "setrlimit": 75,
    "setsid": 66,
    "setsockopt": 366,
    "settimeofday": 79,
    "setuid": 23,
    "setuid32": 213,
    "setxattr": 226,
    "sgetmask": 68,
    "shmat": 397,
    "shmctl": 396,
    "shmdt": 398,
    "shmget": 395,
    "shutdown": 373,
    "sigaction": 67,
    "sigaltstack": 186,
    "signal": 48,
    "signalfd": 321,
    "signalfd4": 327,
    "sigpending": 73,
    "sigprocmask": 126,
    "sigreturn": 119,
    "sigsuspend": 72,
    "socket": 359,
    "socketcall": 102,
    "socketpair": 360,
    "splice": 313,
    "ssetmask": 69,
    "stat": 106,
    "stat64": 195,
    "statfs": 99,
    "statfs64": 268,
    "statx": 383,
    "stime": 25,
    "swapoff": 115,
    "swapon": 87,
    "symlink": 83,
    "symlinkat": 304,
    "sync": 36,
    "sync_file_range": 314,
    "syncfs": 344,
    "sysfs": 135,
    "sysinfo": 116,
    "syslog": 103,
    "tee": 315,
    "tgkill": 270,
    "time": 13,
    "timer_create": 259,
    "timer_delete": 263,
    "timer_getoverrun": 262,
    "timer_gettime": 261,
    "timer_gettime64": 408,
    "timer_settime": 260,
    "timer_settime64": 409,
    "timerfd_create": 322,
    "timerfd_gettime": 326,
    "timerfd_gettime64": 410,
    "timerfd_settime": 325,
    "timerfd_settime64": 411,
    "times": 43,
    "tkill": 238,
    "truncate": 92,
    "truncate64": 193,
    "ugetrlimit": 191,
    "umask": 60,
    "umount": 22,
    "umount2": 52,
    "uname": 122,
    "unlink": 10,
    "unlinkat": 301,
    "unshare": 310,
    "uselib": 86,
    "userfaultfd": 374,
    "ustat": 62,
    "utime": 30,
    "utimensat": 320,
    "utimensat_time64": 412,
    "utimes": 271,
    "vfork": 190,
    "vhangup": 111,
    "vm86": 166,
    "vm86old": 113,
    "vmsplice": 316,
    "wait4": 114,
    "waitid": 284,
    "waitpid": 7,
    "write": 4,
    "writev": 146,
}
