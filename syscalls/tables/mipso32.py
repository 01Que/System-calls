#!/usr/bin/python3

# Content autogenerated. Do not edit.

syscalls_mipso32 = {
    "_llseek": 4140,
    "_newselect": 4142,
    "_sysctl": 4153,
    "accept": 4168,
    "accept4": 4334,
    "access": 4033,
    "acct": 4051,
    "add_key": 4280,
    "adjtimex": 4124,
    "alarm": 4027,
    "bdflush": 4134,
    "bind": 4169,
    "bpf": 4355,
    "brk": 4045,
    "cachectl": 4148,
    "cacheflush": 4147,
    "capget": 4204,
    "capset": 4205,
    "chdir": 4012,
    "chmod": 4015,
    "chown": 4202,
    "chroot": 4061,
    "clock_adjtime": 4341,
    "clock_adjtime64": 4405,
    "clock_getres": 4264,
    "clock_getres_time64": 4406,
    "clock_gettime": 4263,
    "clock_gettime64": 4403,
    "clock_nanosleep": 4265,
    "clock_nanosleep_time64": 4407,
    "clock_settime": 4262,
    "clock_settime64": 4404,
    "clone": 4120,
    "clone3": 4435,
    "close": 4006,
    "close_range": 4436,
    "connect": 4170,
    "copy_file_range": 4360,
    "creat": 4008,
    "create_module": 4127,
    "delete_module": 4129,
    "dup": 4041,
    "dup2": 4063,
    "dup3": 4327,
    "epoll_create": 4248,
    "epoll_create1": 4326,
    "epoll_ctl": 4249,
    "epoll_pwait": 4313,
    "epoll_pwait2": 4441,
    "epoll_wait": 4250,
    "eventfd": 4319,
    "eventfd2": 4325,
    "execve": 4011,
    "execveat": 4356,
    "exit": 4001,
    "exit_group": 4246,
    "faccessat": 4300,
    "faccessat2": 4439,
    "fadvise64": 4254,
    "fallocate": 4320,
    "fanotify_init": 4336,
    "fanotify_mark": 4337,
    "fchdir": 4133,
    "fchmod": 4094,
    "fchmodat": 4299,
    "fchown": 4095,
    "fchownat": 4291,
    "fcntl": 4055,
    "fcntl64": 4220,
    "fdatasync": 4152,
    "fgetxattr": 4229,
    "finit_module": 4348,
    "flistxattr": 4232,
    "flock": 4143,
    "fork": 4002,
    "fremovexattr": 4235,
    "fsconfig": 4431,
    "fsetxattr": 4226,
    "fsmount": 4432,
    "fsopen": 4430,
    "fspick": 4433,
    "fstat": 4108,
    "fstat64": 4215,
    "fstatat64": 4293,
    "fstatfs": 4100,
    "fstatfs64": 4256,
    "fsync": 4118,
    "ftruncate": 4093,
    "ftruncate64": 4212,
    "futex": 4238,
    "futex_time64": 4422,
    "futimesat": 4292,
    "get_kernel_syms": 4130,
    "get_mempolicy": 4269,
    "get_robust_list": 4310,
    "getcpu": 4312,
    "getcwd": 4203,
    "getdents": 4141,
    "getdents64": 4219,
    "getegid": 4050,
    "geteuid": 4049,
    "getgid": 4047,
    "getgroups": 4080,
    "getitimer": 4105,
    "getpeername": 4171,
    "getpgid": 4132,
    "getpgrp": 4065,
    "getpid": 4020,
    "getpmsg": 4208,
    "getppid": 4064,
    "getpriority": 4096,
    "getrandom": 4353,
    "getresgid": 4191,
    "getresuid": 4186,
    "getrlimit": 4076,
    "getrusage": 4077,
    "getsid": 4151,
    "getsockname": 4172,
    "getsockopt": 4173,
    "gettid": 4222,
    "gettimeofday": 4078,
    "getuid": 4024,
    "getxattr": 4227,
    "idle": 4112,
    "init_module": 4128,
    "inotify_add_watch": 4285,
    "inotify_init": 4284,
    "inotify_init1": 4329,
    "inotify_rm_watch": 4286,
    "io_cancel": 4245,
    "io_destroy": 4242,
    "io_getevents": 4243,
    "io_pgetevents": 4368,
    "io_pgetevents_time64": 4416,
    "io_setup": 4241,
    "io_submit": 4244,
    "io_uring_enter": 4426,
    "io_uring_register": 4427,
    "io_uring_setup": 4425,
    "ioctl": 4054,
    "ioperm": 4101,
    "iopl": 4110,
    "ioprio_get": 4315,
    "ioprio_set": 4314,
    "ipc": 4117,
    "kcmp": 4347,
    "kexec_load": 4311,
    "keyctl": 4282,
    "kill": 4037,
    "lchown": 4016,
    "lgetxattr": 4228,
    "link": 4009,
    "linkat": 4296,
    "listen": 4174,
    "listxattr": 4230,
    "llistxattr": 4231,
    "lookup_dcookie": 4247,
    "lremovexattr": 4234,
    "lseek": 4019,
    "lsetxattr": 4225,
    "lstat": 4107,
    "lstat64": 4214,
    "madvise": 4218,
    "mbind": 4268,
    "membarrier": 4358,
    "memfd_create": 4354,
    "migrate_pages": 4287,
    "mincore": 4217,
    "mkdir": 4039,
    "mkdirat": 4289,
    "mknod": 4014,
    "mknodat": 4290,
    "mlock": 4154,
    "mlock2": 4359,
    "mlockall": 4156,
    "mmap": 4090,
    "mmap2": 4210,
    "modify_ldt": 4123,
    "mount": 4021,
    "mount_setattr": 4442,
    "move_mount": 4429,
    "move_pages": 4308,
    "mprotect": 4125,
    "mq_getsetattr": 4276,
    "mq_notify": 4275,
    "mq_open": 4271,
    "mq_timedreceive": 4274,
    "mq_timedreceive_time64": 4419,
    "mq_timedsend": 4273,
    "mq_timedsend_time64": 4418,
    "mq_unlink": 4272,
    "mremap": 4167,
    "msgctl": 4402,
    "msgget": 4399,
    "msgrcv": 4401,
    "msgsnd": 4400,
    "msync": 4144,
    "munlock": 4155,
    "munlockall": 4157,
    "munmap": 4091,
    "name_to_handle_at": 4339,
    "nanosleep": 4166,
    "nfsservctl": 4189,
    "nice": 4034,
    "open": 4005,
    "open_by_handle_at": 4340,
    "open_tree": 4428,
    "openat": 4288,
    "openat2": 4437,
    "pause": 4029,
    "perf_event_open": 4333,
    "personality": 4136,
    "pidfd_getfd": 4438,
    "pidfd_open": 4434,
    "pidfd_send_signal": 4424,
    "pipe": 4042,
    "pipe2": 4328,
    "pivot_root": 4216,
    "pkey_alloc": 4364,
    "pkey_free": 4365,
    "pkey_mprotect": 4363,
    "poll": 4188,
    "ppoll": 4302,
    "ppoll_time64": 4414,
    "prctl": 4192,
    "pread64": 4200,
    "preadv": 4330,
    "preadv2": 4361,
    "prlimit64": 4338,
    "process_madvise": 4440,
    "process_vm_readv": 4345,
    "process_vm_writev": 4346,
    "pselect6": 4301,
    "pselect6_time64": 4413,
    "ptrace": 4026,
    "pwrite64": 4201,
    "pwritev": 4331,
    "pwritev2": 4362,
    "query_module": 4187,
    "quotactl": 4131,
    "quotactl_path": 4443,
    "read": 4003,
    "readahead": 4223,
    "readdir": 4089,
    "readlink": 4085,
    "readlinkat": 4298,
    "readv": 4145,
    "reboot": 4088,
    "recv": 4175,
    "recvfrom": 4176,
    "recvmmsg": 4335,
    "recvmmsg_time64": 4417,
    "recvmsg": 4177,
    "remap_file_pages": 4251,
    "removexattr": 4233,
    "rename": 4038,
    "renameat": 4295,
    "renameat2": 4351,
    "request_key": 4281,
    "restart_syscall": 4253,
    "rmdir": 4040,
    "rseq": 4367,
    "rt_sigaction": 4194,
    "rt_sigpending": 4196,
    "rt_sigprocmask": 4195,
    "rt_sigqueueinfo": 4198,
    "rt_sigreturn": 4193,
    "rt_sigsuspend": 4199,
    "rt_sigtimedwait": 4197,
    "rt_sigtimedwait_time64": 4421,
    "rt_tgsigqueueinfo": 4332,
    "sched_get_priority_max": 4163,
    "sched_get_priority_min": 4164,
    "sched_getaffinity": 4240,
    "sched_getattr": 4350,
    "sched_getparam": 4159,
    "sched_getscheduler": 4161,
    "sched_rr_get_interval": 4165,
    "sched_rr_get_interval_time64": 4423,
    "sched_setaffinity": 4239,
    "sched_setattr": 4349,
    "sched_setparam": 4158,
    "sched_setscheduler": 4160,
    "sched_yield": 4162,
    "seccomp": 4352,
    "semctl": 4394,
    "semget": 4393,
    "semtimedop_time64": 4420,
    "send": 4178,
    "sendfile": 4207,
    "sendfile64": 4237,
    "sendmmsg": 4343,
    "sendmsg": 4179,
    "sendto": 4180,
    "set_mempolicy": 4270,
    "set_robust_list": 4309,
    "set_thread_area": 4283,
    "set_tid_address": 4252,
    "setdomainname": 4121,
    "setfsgid": 4139,
    "setfsuid": 4138,
    "setgid": 4046,
    "setgroups": 4081,
    "sethostname": 4074,
    "setitimer": 4104,
    "setns": 4344,
    "setpgid": 4057,
    "setpriority": 4097,
    "setregid": 4071,
    "setresgid": 4190,
    "setresuid": 4185,
    "setreuid": 4070,
    "setrlimit": 4075,
    "setsid": 4066,
    "setsockopt": 4181,
    "settimeofday": 4079,
    "setuid": 4023,
    "setxattr": 4224,
    "sgetmask": 4068,
    "shmat": 4397,
    "shmctl": 4396,
    "shmdt": 4398,
    "shmget": 4395,
    "shutdown": 4182,
    "sigaction": 4067,
    "sigaltstack": 4206,
    "signal": 4048,
    "signalfd": 4317,
    "signalfd4": 4324,
    "sigpending": 4073,
    "sigprocmask": 4126,
    "sigreturn": 4119,
    "sigsuspend": 4072,
    "socket": 4183,
    "socketcall": 4102,
    "socketpair": 4184,
    "splice": 4304,
    "ssetmask": 4069,
    "stat": 4106,
    "stat64": 4213,
    "statfs": 4099,
    "statfs64": 4255,
    "statx": 4366,
    "stime": 4025,
    "swapoff": 4115,
    "swapon": 4087,
    "symlink": 4083,
    "symlinkat": 4297,
    "sync": 4036,
    "sync_file_range": 4305,
    "syncfs": 4342,
    "syscall": 4000,
    "sysfs": 4135,
    "sysinfo": 4116,
    "syslog": 4103,
    "sysmips": 4149,
    "tee": 4306,
    "tgkill": 4266,
    "time": 4013,
    "timer_create": 4257,
    "timer_delete": 4261,
    "timer_getoverrun": 4260,
    "timer_gettime": 4259,
    "timer_gettime64": 4408,
    "timer_settime": 4258,
    "timer_settime64": 4409,
    "timerfd": 4318,
    "timerfd_create": 4321,
    "timerfd_gettime": 4322,
    "timerfd_gettime64": 4410,
    "timerfd_settime": 4323,
    "timerfd_settime64": 4411,
    "times": 4043,
    "tkill": 4236,
    "truncate": 4092,
    "truncate64": 4211,
    "umask": 4060,
    "umount": 4022,
    "umount2": 4052,
    "uname": 4122,
    "unlink": 4010,
    "unlinkat": 4294,
    "unshare": 4303,
    "uselib": 4086,
    "userfaultfd": 4357,
    "ustat": 4062,
    "utime": 4030,
    "utimensat": 4316,
    "utimensat_time64": 4412,
    "utimes": 4267,
    "vhangup": 4111,
    "vm86": 4113,
    "vmsplice": 4307,
    "wait4": 4114,
    "waitid": 4278,
    "waitpid": 4007,
    "write": 4004,
    "writev": 4146,
}
