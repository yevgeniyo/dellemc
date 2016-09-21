class sds {
  package { 'sds':
    provider => 'rpm',
    ensure => 'present',
    source => '/root/scaleio/sds.rpm',
 }
}




