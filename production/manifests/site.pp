node default { }

node 'host1' {
include mdm
include sds
include sdc
}

node 'host2' {
include mdm
include sds
include sdc
}

node 'host3' {
include sdc
include sds
}



