class mdm {
  package { 'mdm':
    provider => 'rpm',
    ensure => 'present',
    source => '/root/scaleio/mdm.rpm',
 }
}




