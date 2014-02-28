import eSSP
import time

k = eSSP.eSSP('/dev/ttyACM1')
#print k.sync()
#print k.serial_number()
#print k.enable()
#print k.bulb_on()
#print k.bulb_off()
#print k.enable_higher_protocol()
#print k.poll()
#print k.set_inhibits('0xFF', '0xFF')
#print k.set_inhibits(k.easy_inhibit([1, 0, 1]), '0x00')
#print k.unit_data()
#print k.setup_request();
#k.disable();
#k.reset();
#print k.channel_security();
#print k.channel_values();
#print k.channel_reteach();

print 'sync'
print k.sync()
print 'higher protocol'
print k.enable_higher_protocol()
print 'serial'
print k.serial_number()
print 'enable'
print k.enable()
print 'generator'
print k.set_generator()
print 'modolus'
print k.set_modulus()
print 'key exchange'
print k.request_key_exchange()