#!/usr/bin/env ruby

require 'mini_magick'

MAX_SIDE = 200.0

argument = ARGV[0].dup
path = argument.gsub!("\\", "/")
path = path + "/*.{jpg,png,gif}"

Dir.glob(path) do |image|
    puts "Wroking on #{image}"
    thumbname = File.dirname(image) + "/" +
                File.basename(image, ".*") +
                "_thumb" + File.extname(image)

    image_data = MiniMagick::Image.open(image)
    crop_params = "#{MAX_SIDE.to_i}x#{MAX_SIDE.to_i}!"
    puts crop_params
    image_data.crop(crop_params)

    image_data.write(thumbname)

    puts "#{thumbname} written."
end
