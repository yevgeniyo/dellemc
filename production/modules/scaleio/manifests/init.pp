class mdm {
  package { 'mdm':
    provider => rpm,
    ensure => installed,
    source => '~/scaleio/mdm.rpm',
 }
}


class sds {
package { sds:
  provider => 'rpm',
  ensure => installed,
  source => '~/scaleio/sds.rpm',
}
}

class sdc {
package { sdc:
  provider => 'rpm',
  ensure => installed,
  source => '~/scaleio/sdc.rpm',
  install_options => ['MDM_IP=10.136.220.40,10.136.220.41'],
}
}


